import unittest
import json
from app import app


class TestLivros(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.headers = {"Content-Type": "application/json"}

    def tearDown(self):
        pass

    def test_criar_livro(self):
        livro = {
            "titulo": "O Senhor dos Anéis",
            "autor": "J.R.R. Tolkien",
            "ano_publicacao": 1954,
            "isbn": "978-3-16-148410-0",
        }
        response = self.client.post("/livros", json=livro)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn("id", data)
        self.assertEqual(data["titulo"], livro["titulo"])

    def test_listar_livros_vazio(self):
        # TODO: Verificar resposta vazia quando não há livros
        pass

    def test_listar_livros_apos_criacao(self):
        # TODO: Criar livros e verificar se aparecem na listagem
        pass

    def test_obter_livro_existente(self):
        # TODO: Criar um livro e buscá-lo pelo ID
        livro = {
            "titulo": "Dom Casmurro",
            "autor": "Machado de Assis",
            "ano": 1899,
            "isbn": "978-85-359-0277-1",
        }
        post_response = self.client.post(
            "/livros", data=json.dumps(livro), headers=self.headers
        )
        criado = json.loads(post_response.data)

        response = self.client.get(f"/livros/%d" % criado["id"])
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["titulo"], livro["titulo"])

    def test_obter_livro_inexistente(self):
        # TODO: Buscar um ID que não existe
        pass

    def test_remover_livro_existente(self):
        # TODO: Criar um livro e depois removê-lo
        pass

    def test_remover_livro_inexistente(self):
        # TODO: Tentar remover um ID inexistente
        pass

    def test_livro_nao_encontrado_apos_remocao(self):
        # TODO: Verificar que livro removido não pode mais ser consultado
        pass
