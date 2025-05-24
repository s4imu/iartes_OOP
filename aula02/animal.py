class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico")


class Cachorro(Animal):
    def emitir_som(self):
        print("Au au")


class Gata(Animal):
    def emitir_som(self):
        print("Miau")


def chamando_animal(animal: Animal):
    animal.emitir_som()


def main():
    animais = [Cachorro("Rex"), Gata("Mimi"), Animal("Ser")]
    for animalx in animais:
        # print(f"{animal.nome} faz o som: {animal.emitir_som()}")
        chamando_animal(animalx)


if __name__ == "__main__":
    main()
