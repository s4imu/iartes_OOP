"""
Trabalho 03 - Programação Orientada a Objetos
Aluno: Symon Cristhian Ramos Barreto - 1250910
Objetivo deste trabalho é Desenvolver testes automatizados
para a classe implementada na atividade anterior, utilizando
o módulo unittest da linguagem Python. Essa atividade reforça
os conceitos de verificação de comportamento e confiabilidade
de código orientado a objetos.
"""

import unittest
from animal import Animal, Peixe, Pato


class TestAnimal(unittest.TestCase):
    """Classe de testes para verificar o comportamento das classes Animal, Peixe e Pato."""

    def setUp(self):
        """Configuração inicial antes de cada teste."""
        self.animal = Animal("Genérico")
        self.peixe = Peixe("Nemo")
        self.pato = Pato("Donald")

    def tearDown(self):
        """Limpeza após cada teste."""
        del self.animal
        del self.peixe
        del self.pato

    def test_emitir_som_animal(self):
        """Teste para verificar o som genérico do Animal.(comportamento de esperado)"""
        self.assertEqual(self.animal.emitir_som(), "Som genérico")

    def test_emitir_som_peixe(self):
        """Teste para verificar o som emitido pelo Peixe.(comportamento de esperado)"""
        self.assertEqual(self.peixe.emitir_som(), "Glub glub")

    def test_emitir_som_pato(self):
        """Teste para verificar o som emitido pelo Pato.(comportamento de esperado)"""
        self.assertEqual(self.pato.emitir_som(), "Quack quack")

    def test_metodo_especializado_peixe(self):
        """Teste para verificar o método especializado nadar do Peixe.(comportamento de esperado)"""
        self.assertEqual(self.peixe.nadar(), "Nemo está nadando.")

    def test_metodo_especializado_pato(self):
        """Teste para verificar o método especializado voar do Pato.(comportamento de esperado)"""
        self.assertEqual(self.pato.voar(), "Donald está voando.")

    def test_get_nome(self):
        """Teste para verificar o encapsulamento e acesso ao nome."""
        self.assertEqual(self.animal.get_nome(), "Genérico")

    def test_alteracao_estado_interno(self):
        """Teste para verificar a alteração de estado interno."""
        self.animal._nome = "Alterado"  # Alteração direta no atributo protegido
        self.assertEqual(self.animal.get_nome(), "Alterado")


if __name__ == "__main__":
    unittest.main()
