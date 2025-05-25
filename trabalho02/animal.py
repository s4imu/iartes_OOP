"""
Trabalho 02 - Programação Orientada a Objetos
Aluno: Symon Cristhian Ramos Barreto - 1250910
Objetivo deste trabalho é praticar conceitos de encapsulamento,
herança e polimorfismo por meio da definição de uma hierarquia
de classes em Python.
"""


class Animal:
    """Classe base para representar um animal genérico."""

    def __init__(self, nome):
        """Inicializa o animal com um nome."""
        self._nome = nome  # Encapsulamento: atributo protegido (_nome)

    def emitir_som(self):
        """Método que deve ser sobrescrito pelas subclasses para emitir o som do animal."""
        return "Som genérico"  # Método genérico que será sobrescrito

    def get_nome(self):
        """Retorna o nome do animal."""
        return self._nome  #  Encapsulamento: acesso ao atributo protegido


class Peixe(Animal):
    """Classe que representa um peixe, herda de Animal."""

    def emitir_som(self):
        """Método que emite o som característico do peixe."""
        return "Glub glub"  # Polimorfismo: sobrescrita do método emitir_som

    def nadar(self):
        """Método que simula o nado do peixe."""
        return f"{self.get_nome()} está nadando."  # Método especializado


class Pato(Animal):
    """Classe que representa um pato, herda de Animal."""

    def emitir_som(self):
        """Método que emite o som característico do pato."""
        return "Quack quack"  # Polimorfismo: sobrescrita do método emitir_som

    def voar(self):
        """Método que simula o voo do pato."""
        return f"{self.get_nome()} está voando."  # Método especializado


def main():
    """Função principal para testar as classes."""
    peixe = Peixe("Nemo")
    pato = Pato("Donald")

    # Demonstração de polimorfismo e herança
    print(peixe.emitir_som())  # Glub glub
    print(peixe.nadar())  # Nemo está nadando.

    print(pato.emitir_som())  # Quack quack
    print(pato.voar())  # Donald está voando.


if __name__ == "__main__":
    main()
