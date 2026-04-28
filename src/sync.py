def calcular_estoque(estoque_erp, vendas):
    if vendas > estoque_erp:
        raise ValueError("Vendas maiores que estoque")
    return estoque_erp - vendas