"""Classificador de sentimento por lexicon (ABORDAGEM ANTIGA, antes do BERT).
Mantido aqui em velho/ porque 'ainda funciona'. Sem aviso de que foi abandonado."""

POSITIVAS = {"bom", "otimo", "excelente", "gostei", "recomendo", "rapido"}
NEGATIVAS = {"ruim", "pessimo", "horrivel", "lento", "caro", "quebrado"}


def classificar(texto: str) -> str:
    t = texto.lower().split()
    pos = sum(1 for w in t if w in POSITIVAS)
    neg = sum(1 for w in t if w in NEGATIVAS)
    if pos > neg:
        return "positivo"
    if neg > pos:
        return "negativo"
    return "neutro"


if __name__ == "__main__":
    print(classificar("o produto e bom e rapido mas o suporte e lento"))
