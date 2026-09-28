"""Ordenador temporal por dependência de estado (protótipo da ONTOLOGIA v0).

Recebe cenas já estruturadas (evento, pré-condições, adiciona, remove, timestamp opcional) e
calcula, sem usar o timestamp como chave de ordem:
  - a ordem parcial (fecho transitivo de "habilita": efeito de A satisfaz pré-condição de B);
  - pares incomparáveis (sem dependência; não é "simultâneo");
  - lacunas (pré-condição sem produtor e fora do estado inicial) -> pergunta concreta;
  - intrusos (evento sem ligação com o episódio);
  - conflitos (ciclo; timestamp contra a cadeia; ameaça simples);
  - ambiguidade restante (número de extensões lineares, em bits).
A extração das cenas a partir de texto ou imagem (papel do LLM) fica fora: ver ONTOLOGIA.md §7.
Só biblioteca padrão. Uso: python ordenador.py
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from functools import lru_cache
from itertools import combinations


@dataclass
class Evento:
    nome: str
    pre: set[str] = field(default_factory=set)
    adiciona: set[str] = field(default_factory=set)
    remove: set[str] = field(default_factory=set)
    ts: float | None = None          # timestamp observado: evidência revogável, não chave
    origem: str = "observado"        # observado | inferido (regra 6)


@dataclass
class Resultado:
    arestas: set[tuple[str, str]]
    antes: set[tuple[str, str]]
    incomparaveis: list[tuple[str, str]]
    lacunas: list[tuple[str, str]]           # (fluente, quem precisa)
    produtor_ambiguo: list[tuple[str, str, list[str]]]
    intrusos: list[str]
    conflitos: list[str]
    ordens: int
    bits: float
    bits_norm: float
    uma_ordem: list[str]


def analisar(eventos: list[Evento], inicial: set[str]) -> Resultado:
    nomes = [e.nome for e in eventos]
    por_nome = {e.nome: e for e in eventos}
    produtores: dict[str, list[str]] = {}
    for e in eventos:
        for p in e.adiciona:
            produtores.setdefault(p, []).append(e.nome)

    arestas: set[tuple[str, str]] = set()
    lacunas, ambiguos = [], []
    for e in eventos:
        for p in sorted(e.pre):
            prods = [n for n in produtores.get(p, []) if n != e.nome]
            if len(prods) == 1:
                arestas.add((prods[0], e.nome))
            elif len(prods) > 1:
                ambiguos.append((p, e.nome, prods))
            elif p not in inicial:
                lacunas.append((p, e.nome))

    conflitos: list[str] = []
    # ciclo (Kahn)
    grau = {n: 0 for n in nomes}
    for _, b in arestas:
        grau[b] += 1
    fila = sorted(n for n in nomes if grau[n] == 0)
    uma_ordem = []
    while fila:
        n = fila.pop(0)
        uma_ordem.append(n)
        for a, b in sorted(arestas):
            if a == n:
                grau[b] -= 1
                if grau[b] == 0:
                    fila.append(b)
        fila.sort()
    if len(uma_ordem) < len(nomes):
        conflitos.append("ciclo de dependência: " + ", ".join(n for n in nomes if n not in uma_ordem))

    # fecho transitivo
    antes = set(arestas)
    mudou = True
    while mudou:
        mudou = False
        for a, b in list(antes):
            for c, d in list(antes):
                if b == c and (a, d) not in antes:
                    antes.add((a, d))
                    mudou = True

    incomparaveis = [(a, b) for a, b in combinations(nomes, 2)
                     if (a, b) not in antes and (b, a) not in antes]

    # timestamp contra a cadeia (regra 2: o timestamp é o suspeito)
    for a, b in sorted(antes):
        ta, tb = por_nome[a].ts, por_nome[b].ts
        if ta is not None and tb is not None and ta > tb:
            conflitos.append(f"timestamp contra a cadeia: '{a}' ({ta}) precisa vir antes de '{b}' ({tb})")

    # ameaça simples: d remove p entre o produtor a e o consumidor c, forçado pela ordem
    for a, c in arestas:
        for p in por_nome[a].adiciona & por_nome[c].pre:
            for d in nomes:
                if d not in (a, c) and p in por_nome[d].remove and (a, d) in antes and (d, c) in antes:
                    conflitos.append(f"ameaça: '{d}' remove '{p}' entre '{a}' e '{c}'")

    ligados = {x for par in arestas for x in par}
    intrusos = [n for n in nomes if n not in ligados] if len(nomes) > 1 else []

    ordens = contar_extensoes(tuple(nomes), frozenset(antes)) if not conflitos or all(
        not c.startswith("ciclo") for c in conflitos) else 0
    bits = math.log2(ordens) if ordens else float("nan")
    bits_norm = bits / math.log2(math.factorial(len(nomes))) if len(nomes) > 1 and ordens else 0.0
    return Resultado(arestas, antes, incomparaveis, lacunas, ambiguos, intrusos, conflitos,
                     ordens, bits, bits_norm, uma_ordem)


def contar_extensoes(nomes: tuple[str, ...], antes: frozenset) -> int:
    """Conta ordens totais compatíveis (DP sobre subconjuntos; ok até ~20 eventos)."""
    idx = {n: i for i, n in enumerate(nomes)}
    pred = [0] * len(nomes)
    for a, b in antes:
        pred[idx[b]] |= 1 << idx[a]

    @lru_cache(maxsize=None)
    def f(feitos: int) -> int:
        if feitos == (1 << len(nomes)) - 1:
            return 1
        return sum(f(feitos | 1 << i) for i in range(len(nomes))
                   if not feitos >> i & 1 and pred[i] & feitos == pred[i])

    return f(0)


def relatorio(titulo: str, eventos: list[Evento], inicial: set[str]) -> Resultado:
    r = analisar(eventos, inicial)
    print(f"\n=== {titulo} ===")
    print("entrada (ordem de leitura):", ", ".join(
        f"{e.nome}{'' if e.ts is None else f'@{e.ts}'}{'' if e.origem == 'observado' else ' [inferido]'}"
        for e in eventos))
    print("habilita:", ", ".join(f"{a} -> {b}" for a, b in sorted(r.arestas)) or "(nada)")
    print("uma ordem compatível:", " -> ".join(r.uma_ordem))
    print("incomparáveis (não simultâneos):", ", ".join(f"{a} || {b}" for a, b in r.incomparaveis) or "(nenhum)")
    print(f"ordens compatíveis: {r.ordens}  (ambiguidade {r.bits:.2f} bits; normalizada {r.bits_norm:.2f})")
    faltam: dict[str, list[str]] = {}
    for p, quem in r.lacunas:
        faltam.setdefault(p, []).append(quem)
    for p, quem in faltam.items():
        print(f"LACUNA: {quem} precisam de '{p}', e nada produz isso -> perguntar: o que produz '{p}'?")
    for p, quem, prods in r.produtor_ambiguo:
        print(f"PRODUTOR AMBÍGUO: '{p}' para '{quem}' vem de {prods}")
    for n in r.intrusos:
        print(f"INTRUSO: '{n}' não se liga ao episódio")
    for c in r.conflitos:
        print("CONFLITO:", c)
    return r


def paraquedas() -> list[Evento]:
    return [
        Evento("abrir", {"em_queda"}, {"velame_aberto"}),
        Evento("embarcar", {"no_chao", "tem_bilhete"}, {"a_bordo"}, {"no_chao"}),
        Evento("saltar", {"a_bordo", "em_altitude", "paraquedas_vestido"}, {"em_queda"}, {"a_bordo"}),
        Evento("vestir_paraquedas", {"tem_paraquedas"}, {"paraquedas_vestido"}),
        Evento("decolar_e_subir", {"a_bordo"}, {"em_altitude"}),
    ]


INICIAL = {"no_chao", "tem_bilhete", "tem_paraquedas"}

# script conhecido (prior): quem costuma produzir cada fluente. Serve para PROPOR, não para observar.
SCRIPT = {"a_bordo": Evento("embarcar", {"no_chao", "tem_bilhete"}, {"a_bordo"}, {"no_chao"},
                            origem="inferido")}


def main() -> None:
    # 1. embaralhado e com horários trocados
    ev = paraquedas()
    # um único horário trocado: 'abrir' anotado antes de 'saltar'
    ts = {"vestir_paraquedas": 8.50, "embarcar": 8.55, "decolar_e_subir": 9.00, "saltar": 9.20, "abrir": 9.10}
    for e in ev:
        e.ts = ts[e.nome]
    relatorio("1. cenas embaralhadas, um horário trocado", ev, INICIAL)

    # 2. passo removido sem aviso
    ev = [e for e in paraquedas() if e.nome != "embarcar"]
    r = relatorio("2. 'embarcar' removido sem aviso", ev, INICIAL)

    # 2b. preencher a lacuna pelo script, marcando como inferido (regra 6)
    for p, _ in r.lacunas[:1]:
        if p in SCRIPT:
            relatorio("2b. lacuna preenchida pelo script (inferido, não observado)", ev + [SCRIPT[p]], INICIAL)

    # 3. passo intruso
    ev = paraquedas() + [Evento("pedir_pizza", {"com_fome"}, {"pizza"})]
    relatorio("3. passo intruso no meio", ev, INICIAL | {"com_fome"})


if __name__ == "__main__":
    main()
