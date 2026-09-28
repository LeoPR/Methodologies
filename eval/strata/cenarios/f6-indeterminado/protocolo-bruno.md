# Protocolo (Bruno)

- Dados: leituras a cada minuto dos 3 sensores da câmara.
- Janela de análise: 5 minutos.
- Detecção: leitura acima de 2,5 desvios-padrão da média da janela.
- Métrica: F1 sobre os eventos anotados pela manutenção.
- Alertas repetidos dentro de 15 minutos contam como um só.
