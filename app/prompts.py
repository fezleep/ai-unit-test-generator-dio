try:
    from langchain_core.prompts import PromptTemplate
except ImportError:
    from langchain.prompts import PromptTemplate


TEST_GENERATION_TEMPLATE = """
voce e um assistente especialista em python e pytest.

gere testes unitarios para o arquivo abaixo.

regras:
- use pytest
- inclua import pytest
- crie funcoes com prefixo test_
- cubra casos de sucesso
- cubra pelo menos um caso de erro quando fizer sentido
- retorne somente codigo python valido
- nao use markdown

arquivo: {file_name}

codigo:
{source_code}
"""


def build_test_generation_prompt(file_name, source_code):
    prompt = PromptTemplate.from_template(TEST_GENERATION_TEMPLATE)
    return prompt.format(file_name=file_name, source_code=source_code)
