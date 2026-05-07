def calcular_estoque(estoque_erp: int, vendas: int, devolucoes: int = 0, margem_seguranca: int = 0) -> int:
    """
    Calcula o saldo atualizado do estoque após o registro de vendas e devoluções.
    Garante que o estoque não fique negativooo e respeita a margem de segurança do E-commerce.
    """
    estoque_real = estoque_erp + devolucoes
    estoque_disponivel_venda = estoque_real - margem_seguranca
    
    if vendas > estoque_disponivel_venda:
        raise ValueError(f"Venda ({vendas}) não permitida. Estoque disponível para venda é {estoque_disponivel_venda}.")
        
    return estoque_real - vendas