class Produto:
    def __init__(self, nome, valido, qtde):
        self.__validade = valido  # Atributo privado
        self.nome = nome  # Atributo público
        self._qtde = qtde  # Atributo protegido

    @property
    def validade(self):
        return self.__validade

    @validade.setter
    def validade(self, validade):
        if self.__validar_data(validade):
            self.__validade = validade

    def entrada_produto(self, qtde):
        if qtde > 0:
            self._qtde += qtde

    def saida_produto(self, qtde):
        if qtde <= self._qtde:
            self._qtde -= qtde
            return True
        return False

    def __validar_data(self, validade):
        return True


def main():
    p = Produto("Arroz", "2025/06/01", 100)
    p.validade = "2025/12/31"
    print(p.validade)
    # print(f"Produto: {p.nome}, Validade: {p.validade}, Quantidade: {p._qtde}")


if __name__ == "__main__":
    main()
