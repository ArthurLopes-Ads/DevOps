import pytest
from src.sync import calcular_estoque

def test_calcular_estoque_sucesso():
    resultado = calcular_estoque(50, 10)
    assert resultado == 40

def test_calcular_estoque_erro():
    with pytest.raises(ValueError):
        calcular_estoque(10, 20)