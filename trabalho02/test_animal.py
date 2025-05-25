import unittest
from animal import Animal, Cachorro, Gata

class TesteAnimal(unittest.TestCase):
    def test_emitir_som_animal(self):
        a = Animal("Bicho")
        self.assertEqual(a.emitir_som(), "Som genérico")

    def test_emitir_som_cachorro(self):
        c = Cachorro("Rex")
        self.assertEqual(c.emitir_som(), "Au au")

    def test_emitir_som_gata(self):
        g = Gata("Mimi")
        self.assertEqual(g.emitir_som(), "Miau")

    def test_get_nome(self):
        c = Cachorro("Toby")
        self.assertEqual(c.get_nome(), "Toby")

if __name__ == "__main__":
    unittest.main()
