import ast
from pathlib import Path


class MockLLM:
    def invoke(self, prompt):
        file_name = self._extract_file_name(prompt)

        if file_name == "calculator.py":
            return self._calculator_tests()

        if file_name == "string_utils.py":
            return self._string_utils_tests()

        return self._generic_tests(prompt, file_name)

    def _extract_file_name(self, prompt):
        for line in prompt.splitlines():
            if line.startswith("arquivo:"):
                return line.replace("arquivo:", "").strip()

        return "arquivo.py"

    def _extract_source_code(self, prompt):
        marker = "codigo:"
        if marker not in prompt:
            return ""

        return prompt.split(marker, 1)[1].strip()

    def _generic_tests(self, prompt, file_name):
        source_code = self._extract_source_code(prompt)
        module_name = Path(file_name).stem

        try:
            tree = ast.parse(source_code)
        except SyntaxError:
            return "import pytest\n\n\ndef test_codigo_python_deve_ser_valido():\n    assert False\n"

        functions = [
            node.name
            for node in tree.body
            if isinstance(node, ast.FunctionDef) and not node.name.startswith("_")
        ]

        if not functions:
            return "import pytest\n\n\ndef test_arquivo_deve_ter_funcoes_publicas():\n    assert True\n"

        imports = ", ".join(functions)
        tests = ["import pytest", "", f"from examples.{module_name} import {imports}", ""]

        for function_name in functions:
            tests.append("")
            tests.append(f"def test_{function_name}_deve_existir():")
            tests.append(f"    assert callable({function_name})")

        return "\n".join(tests)

    def _calculator_tests(self):
        return """import pytest

from examples.calculator import divisao, multiplicacao, soma, subtracao


def test_soma_deve_retornar_resultado_correto():
    assert soma(2, 3) == 5


def test_soma_deve_funcionar_com_numero_negativo():
    assert soma(-2, 3) == 1


def test_subtracao_deve_retornar_resultado_correto():
    assert subtracao(10, 4) == 6


def test_multiplicacao_deve_retornar_resultado_correto():
    assert multiplicacao(3, 4) == 12


def test_divisao_deve_retornar_resultado_correto():
    assert divisao(10, 2) == 5


def test_divisao_deve_lancar_erro_quando_divisor_for_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)
"""

    def _string_utils_tests(self):
        return """import pytest

from examples.string_utils import (
    contar_caracteres,
    inverter_texto,
    transformar_para_maiusculo,
)


def test_inverter_texto_deve_retornar_texto_invertido():
    assert inverter_texto("python") == "nohtyp"


def test_inverter_texto_deve_funcionar_com_texto_vazio():
    assert inverter_texto("") == ""


def test_contar_caracteres_deve_retornar_tamanho_do_texto():
    assert contar_caracteres("dio") == 3


def test_contar_caracteres_deve_contar_espacos():
    assert contar_caracteres("teste unitario") == 14


def test_transformar_para_maiusculo_deve_retornar_texto_em_maiusculo():
    assert transformar_para_maiusculo("langchain") == "LANGCHAIN"


def test_transformar_para_maiusculo_deve_lancar_erro_com_valor_none():
    with pytest.raises(AttributeError):
        transformar_para_maiusculo(None)
"""
