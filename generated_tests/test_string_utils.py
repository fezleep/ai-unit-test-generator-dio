import pytest

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
