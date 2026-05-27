# ai-unit-test-generator-dio

projeto de estudo para gerar testes unitarios automaticamente com python, langchain e uma estrutura preparada para azure openai.

a ideia e simples: o programa le um arquivo python, monta um prompt com instrucoes para criacao de testes e salva um arquivo `test_*.py` pronto para rodar com pytest.

por enquanto, o projeto usa um mock llm local. isso deixa tudo mais facil de executar, sem depender de chave da azure, conta ativa ou consumo de api. mesmo assim, a organizacao ja deixa claro onde uma integracao real com azure openai entraria depois.

## objetivo

criar um agente simples em python capaz de:

- ler um arquivo `.py`
- gerar testes unitarios com pytest
- salvar os testes em `generated_tests/`
- cobrir casos de sucesso
- cobrir casos de erro quando fizer sentido
- manter uma arquitetura simples para evoluir para azure openai

## como funciona

o fluxo principal fica em `app/generator.py`.

ele faz quatro coisas:

1. le o arquivo python de entrada
2. monta um prompt usando `app/prompts.py`
3. chama o `MockLLM`, que simula a resposta de um modelo
4. salva o teste gerado na pasta `generated_tests/`

os exemplos ficam em `examples/` e os testes gerados ficam em `generated_tests/`.

## arquitetura

```text
ai-unit-test-generator-dio/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── docs/
│   └── entrega_dio.md
├── examples/
│   ├── calculator.py
│   └── string_utils.py
├── generated_tests/
│   ├── test_calculator.py
│   └── test_string_utils.py
├── app/
│   ├── generator.py
│   ├── prompts.py
│   ├── mock_llm.py
│   └── utils.py
└── README-assets/
    └── .gitkeep
```

## uso do langchain

o langchain aparece na montagem do prompt, usando `PromptTemplate`.

isso deixa o prompt separado do codigo principal e facilita ajustes na engenharia de prompts sem mexer no fluxo do gerador.

o projeto ainda nao chama um modelo real. essa decisao foi intencional para manter o desafio executavel em qualquer maquina.

## integracao futura com azure

o arquivo `.env.example` ja traz as variaveis esperadas para uma futura integracao:

```env
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_KEY=
AZURE_OPENAI_DEPLOYMENT=
```

em uma evolucao natural, o `MockLLM` pode ser trocado por uma classe usando azure openai. o restante do fluxo pode continuar praticamente igual.

## engenharia de prompts

o prompt pede que a resposta tenha:

- codigo python valido
- testes com pytest
- funcoes com prefixo `test_`
- casos positivos
- casos de erro quando fizer sentido
- nenhum markdown na resposta

isso ajuda a gerar um arquivo que possa ser salvo e executado diretamente.

## como executar

crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

no windows:

```bash
.venv\Scripts\activate
```

instale as dependencias:

```bash
pip install -r requirements.txt
```

gere testes para o exemplo da calculadora:

```bash
python -m app.generator examples/calculator.py
```

gere testes para o exemplo de texto:

```bash
python -m app.generator examples/string_utils.py
```

## como rodar pytest

execute:

```bash
pytest
```

ou rode apenas a pasta de testes gerados:

```bash
pytest generated_tests
```

## exemplos

`examples/calculator.py` contem funcoes simples de calculadora:

- soma
- subtracao
- multiplicacao
- divisao

a funcao `divisao` lanca `ValueError` quando o divisor e zero.

`examples/string_utils.py` contem funcoes simples para texto:

- inverter texto
- contar caracteres
- transformar para maiusculo

## prints do projeto

sugestao de prints para colocar na entrega:

- estrutura de pastas no editor
- terminal rodando `python -m app.generator examples/calculator.py`
- terminal rodando `python -m app.generator examples/string_utils.py`
- terminal com o resultado do `pytest`
- arquivo `generated_tests/test_calculator.py` aberto
- arquivo `generated_tests/test_string_utils.py` aberto

## aprendizados

este projeto ajuda a praticar a ligacao entre ia generativa e testes automatizados.

mesmo com um mock llm, o fluxo mostra bem a ideia principal: transformar codigo fonte em um prompt, gerar testes e validar tudo com pytest.

tambem fica claro que bons prompts precisam ser objetivos. quanto mais direta for a instrucao, maior a chance de receber um teste util e executavel.

## proximos passos

- criar uma classe real para azure openai
- permitir escolher entre mock e azure via `.env`
- melhorar a analise do codigo com `ast`
- gerar testes para mais tipos de funcoes
- adicionar validacao automatica do codigo gerado

## conclusao

o projeto e educacional, simples e focado em pratica.

ele nao tenta ser uma ferramenta completa de mercado. o objetivo e mostrar, de forma organizada, como python, langchain, prompts e pytest podem trabalhar juntos para automatizar parte da criacao de testes unitarios.
