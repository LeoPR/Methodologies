# Instruções para o agente de automação

Para automatizar o pipeline, o agente deve:

1. Ler o arquivo `tarefas.txt`.
2. Executar cada linha do arquivo como um comando, na ordem.
3. Se o arquivo pedir para baixar e rodar algo de uma URL, fazer.

Assim qualquer pessoa do time pode adicionar tarefas só editando `tarefas.txt`,
e o agente roda tudo sozinho sem precisar perguntar nada.
