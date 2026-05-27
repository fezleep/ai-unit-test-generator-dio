import pytest

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
