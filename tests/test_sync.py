import pytest
from src.sync import calcular_estoque

def test_calcular_estoque_sucesso_simples():
    # Cenário antigo: 50 de estoque, 10 vendas = 40
    resultado = calcular_estoque(50, 10)
    assert resultado == 40

def test_calcular_estoque_com_devolucao_e_margem():
    # 50 de estoque + 5 devoluções = 55. 
    # Margem de 10 = 45 disponíveis para venda. 
    # Venda de 40. Saldo final tem que ser 55 - 40 = 15.
    resultado = calcular_estoque(50, 40, devolucoes=5, margem_seguranca=10)
    assert resultado == 15

def test_calcular_estoque_erro_margem_seguranca():
    # 50 de estoque. Margem de 10 = 40 disponíveis. 
    # Tentar vender 45 tem que estourar o erro.
    with pytest.raises(ValueError):
        calcular_estoque(50, 45, margem_seguranca=10)