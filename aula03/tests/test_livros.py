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

    def test_01_listar_livros_vazio(self):
        # TODO: Verificar resposta vazia quando não há livros
        get_response = self.client.get("/livros")
        self.assertEqual(get_response.status_code, 200)
        data = json.loads(get_response.data)
        self.assertEqual(data, {"livros": []})

    def test_02_criar_livro(self):
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

    def test_03_listar_livros_apos_criacao(self):
        # TODO: Criar livros e verificar se aparecem na listagem

        livro = {
            "titulo": "1984",
            "autor": "George Orwell",
            "ano_publicacao": 1949,
            "isbn": "978-0-452-28423-4",
        }
        response = self.client.post(
            "/livros", data=json.dumps(livro), headers=self.headers
        )
        self.assertEqual(response.status_code, 201)
        livros_response = self.client.get("/livros")
        self.assertEqual(livros_response.status_code, 200)
        data = json.loads(livros_response.data)
        livros = data["livros"]
        self.assertTrue(
            any(
                l["titulo"] == livro["titulo"] and l["autor"] == livro["autor"]
                for l in livros
            )
        )
    def test_04_obter_livro_existente(self):
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

    def test_05_obter_livro_inexistente(self):
        # TODO: Buscar um ID que não existe
        response = self.client.get("/livros/9999")
        self.assertEqual(response.status_code, 404)

    def test_06_remover_livro_existente(self):
        # TODO: Criar um livro e depois removê-lo
        livro = {
            "titulo": "O Alquimista",
            "autor": "Paulo Coelho",
            "ano_publicacao": 1988,
            "isbn": "978-85-325-7322-3",
        }
        post_response = self.client.post(
            "/livros", data=json.dumps(livro), headers=self.headers
        )
        criado = json.loads(post_response.data)

        response = self.client.get(f"/livros/%d" % criado["id"])
        self.assertEqual(response.status_code, 200)

        del_response = self.client.delete(f"/livros/%d" % criado["id"])
        self.assertEqual(del_response.status_code, 204)

    def test_07_remover_livro_inexistente(self):
        # TODO: Tentar remover um ID inexistente
        response = self.client.delete("/livros/9999")
        self.assertEqual(response.status_code, 404)

    def test_08_livro_nao_encontrado_apos_remocao(self):
        # TODO: Verificar que livro removido não pode mais ser consultado
        livro = {
            "titulo": "O Alquimista",
            "autor": "Paulo Coelho",
            "ano_publicacao": 1988,
            "isbn": "978-85-325-7322-3",
        }
        post_response = self.client.post(
            "/livros", data=json.dumps(livro), headers=self.headers
        )
        criado = json.loads(post_response.data)

        response = self.client.get(f"/livros/%d" % criado["id"])
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        id = data["id"]
        response = self.client.delete(f"/livros/{id}")
        self.assertEqual(response.status_code, 204)
        response = self.client.get(f"/livros/{id}")
        self.assertEqual(response.status_code, 404)
