class Funcionario:
    def __init__(self, salario: float):
        """Um atributo privado __salario"""
        self.__salario = salario

    # um método privado __calcular_bonus() que retorna 10% do salário
    def __calcular_bonus(self) -> float:
        return self.__salario * 0.1

    # uma propriedade salario com getter e setter para controle de acesso
    @property
    def salario(self) -> float:
        return self.__salario

    @salario.setter
    def salario(self, salario: float) -> None:
        if salario > 0:
            self.__salario = salario

    # um método público aumentar_salario(percentual: int)
    def aumentar_salario(self, percentual: int) -> None:
        if percentual > 0:
            novo_salario = self.salario * (1 + percentual / 100)
            self.salario = novo_salario
        else:
            raise ValueError("O percentual deve ser maior que zero.")


def main() -> None:
    f = Funcionario(1000.0)
    print(f"Salário inicial: {f.salario}")

    f.aumentar_salario(20)
    print(f"Salário após aumento: {f.salario}")

    try:
        f.aumentar_salario(-5)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
