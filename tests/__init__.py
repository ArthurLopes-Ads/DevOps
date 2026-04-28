from src.sync import calcular_estoque

def main():
    estoque_atual = calcular_estoque(100, 20)
    print(f"Estoque sincronizado: {estoque_atual}")

if __name__ == "__main__":
    main()