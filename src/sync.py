def calcular_estoque(estoque_erp: int, vendas: int) -> int:
    """
    Calcula o saldo atualizado do estoque após o registro de vendas.
    Garante que o estoque não fique negativo, evitando falhas na sincronização.
    """
    if vendas > estoque_erp:
        raise ValueError("Vendas maiores que estoque")
    return estoque_erp - vendas