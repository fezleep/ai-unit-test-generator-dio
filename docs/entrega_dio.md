# entrega dio

este projeto cria um gerador simples de testes unitarios com python, langchain e pytest.

a ideia foi simular um agente capaz de ler um arquivo `.py`, montar um prompt com boas instrucoes e gerar um arquivo `test_*.py` dentro da pasta `generated_tests`.

para nao depender de uma conta real da azure openai, o projeto usa um mock llm local. ele devolve testes prontos para os exemplos do projeto e permite validar o fluxo completo: leitura do arquivo, criacao do prompt, geracao do teste e execucao com pytest.

mesmo usando mock, a arquitetura ja deixa um ponto claro para trocar esse componente por uma integracao real com azure openai no futuro.

o foco principal foi praticar:

- automacao de testes
- pytest
- langchain
- engenharia de prompts
- organizacao de um projeto python simples
- preparacao para uso futuro com azure openai

os testes gerados cobrem casos positivos e alguns casos de erro, como divisao por zero e entrada invalida em funcoes de texto.
