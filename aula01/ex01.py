"""Este módulo cria uma lista de números pares de 0 a 19 e imprime a lista invertida."""

def main():
    """Gera uma lista de números pares de 0 a 19, a inverte e imprime."""
    lista = [x for x in range(20) if x % 2 == 0]
    lista_revertida = list(reversed(lista))
    print(lista_revertida)

if __name__ == "__main__":
    main()
