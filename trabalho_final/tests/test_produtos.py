import unittest
import json
from app import app


class TestEstoque(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.headers = {"Content-Type": "application/json"}

    # Cenários de Sucesso
    def test_CT001_criar_produto_valido(self):
        produto = {
            "nome": "Notebook",
            "categoria": "Eletrônicos",
            "quantidade_inicial": 10,
            "preco_unitario": 2500.00,
        }
        response = self.client.post(
            "/produtos", data=json.dumps(produto), headers=self.headers
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data["nome"], produto["nome"])

    def test_CT002_listar_produtos(self):
        response = self.client.get("/produtos")
        self.assertEqual(response.status_code, 200)

    def test_CT003_buscar_produto(self):
        produto = {
            "nome": "Notebook",
            "categoria": "Eletrônicos",
            "quantidade_inicial": 10,
            "preco_unitario": 2500.00,
        }
        self.client.post("/produtos", data=json.dumps(produto), headers=self.headers)
        response = self.client.get("/produtos/1", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["nome"], produto["nome"])

    def test_CT004_buscar_produtos_com_filtro(self):
        produto1 = {
            "nome": "Notebook",
            "categoria": "Eletrônicos",
            "quantidade_inicial": 10,
            "preco_unitario": 2500.00,
        }
        produto2 = {
            "nome": "Smartphone",
            "categoria": "Eletrônicos",
            "quantidade_inicial": 20,
            "preco_unitario": 1500.00,
        }
        self.client.post("/produtos", data=json.dumps(produto1), headers=self.headers)
        self.client.post("/produtos", data=json.dumps(produto2), headers=self.headers)
        response = self.client.get(
            "/produtos?categoria=Eletrônicos", headers=self.headers
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)

    def test_CT005_atualizar_produto(self):
        produto = {
            "nome": "Notebook",
            "categoria": "Eletrônicos",
            "quantidade_inicial": 10,
            "preco_unitario": 2500.00,
        }
        self.client.post("/produtos", data=json.dumps(produto), headers=self.headers)
        atualizacao = {"nome": "Notebook Pro", "preco_unitario": 3000.00}
        response = self.client.put(
            "/produtos/1", data=json.dumps(atualizacao), headers=self.headers
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["nome"], "Notebook Pro")

    def test_CT006_entrada_estoque(self):
        produto = {
            "nome": "Notebook",
            "categoria": "Eletrônicos",
            "quantidade_inicial": 10,
            "preco_unitario": 2500.00,
        }
        self.client.post("/produtos", data=json.dumps(produto), headers=self.headers)
        response = self.client.post(
            "/produtos/1/entrada",
            data=json.dumps({"quantidade": 5}),
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["quantidade_inicial"], 15)

    def test_CT007_saida_estoque(self):
        produto = {
            "nome": "Notebook",
            "categoria": "Eletrônicos",
            "quantidade_inicial": 10,
            "preco_unitario": 2500.00,
        }
        self.client.post("/produtos", data=json.dumps(produto), headers=self.headers)
        response = self.client.post(
            "/produtos/1/saida",
            data=json.dumps({"quantidade": 5}),
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["quantidade_inicial"], 5)

    def test_CT008_remover_produto(self):
        produto = {
            "nome": "Notebook",
            "categoria": "Eletrônicos",
            "quantidade_inicial": 10,
            "preco_unitario": 2500.00,
        }
        self.client.post("/produtos", data=json.dumps(produto), headers=self.headers)
        response = self.client.delete("/produtos/1", headers=self.headers)
        self.assertEqual(response.status_code, 200)

    # Cenários de Erro de Validação
    def test_CT009_cadastrar_produto_sem_dados(self):
        response = self.client.post("/produtos", headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_CT010_criar_produto_invalido(self):
        produto = {
            "nome": "Notebook",
            "categoria": "Eletrônicos",
            "quantidade_inicial": -5,
            "preco_unitario": 2500.00,
        }
        response = self.client.post(
            "/produtos", data=json.dumps(produto), headers=self.headers
        )
        self.assertEqual(response.status_code, 400)

    def test_CT011_entrada_estoque_invalida(self):
        produto = {
            "nome": "Notebook",
            "categoria": "Eletrônicos",
            "quantidade_inicial": 10,
            "preco_unitario": 2500.00,
        }
        self.client.post("/produtos", data=json.dumps(produto), headers=self.headers)
        response = self.client.post(
            "/produtos/1/entrada",
            data=json.dumps({"quantidade": -5}),
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn("Quantidade inválida", data["error"])

    def test_CT012_atualizar_produto_com_dados_invalidos(self):
        produto = {
            "nome": "Notebook",
            "categoria": "Eletrônicos",
            "quantidade_inicial": 10,
            "preco_unitario": 2500.00,
        }
        self.client.post("/produtos", data=json.dumps(produto), headers=self.headers)
        atualizacao = {"nome": "", "preco_unitario": -3000.00}
        response = self.client.put(
            "/produtos/1", data=json.dumps(atualizacao), headers=self.headers
        )
        self.assertEqual(response.status_code, 400)

    def test_CT013_atualizar_produto_sem_dados(self):
        response = self.client.put("/produtos/1", headers=self.headers)
        self.assertEqual(response.status_code, 400)

    # Cenários de Requisições Inválidas
    def test_CT014_buscar_produto_inexistente(self):
        response = self.client.get("/produtos/999", headers=self.headers)
        self.assertEqual(response.status_code, 404)

    def test_CT015_buscar_produtos_com_parametros_invalidos(self):
        response = self.client.get(
            "/produtos?filtroInvalido=Inexistente", headers=self.headers
        )
        self.assertEqual(response.status_code, 404)

    def test_CT016_atualizar_produto_inexistente(self):
        atualizacao = {"nome": "Notebook Pro", "preco_unitario": 3000.00}
        response = self.client.put(
            "/produtos/999", data=json.dumps(atualizacao), headers=self.headers
        )
        self.assertEqual(response.status_code, 404)

    def test_CT017_remover_produto_inexistente(self):
        response = self.client.delete("/produtos/999", headers=self.headers)
        self.assertEqual(response.status_code, 404)

    # Cenários de Operações com Estoque Zerado ou Negativo
    def test_CT018_saida_estoque_insuficiente(self):
        produto = {
            "nome": "Notebook",
            "categoria": "Eletrônicos",
            "quantidade_inicial": 5,
            "preco_unitario": 2500.00,
        }
        self.client.post("/produtos", data=json.dumps(produto), headers=self.headers)
        response = self.client.post(
            "/produtos/1/saida",
            data=json.dumps({"quantidade": 10}),
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn("Estoque insuficiente", data["error"])

    def test_CT019_saida_estoque_zerado(self):
        produto = {
            "nome": "Notebook",
            "categoria": "Eletrônicos",
            "quantidade_inicial": 0,
            "preco_unitario": 2500.00,
        }
        self.client.post("/produtos", data=json.dumps(produto), headers=self.headers)
        response = self.client.post(
            "/produtos/1/saida",
            data=json.dumps({"quantidade": 5}),
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn("Estoque insuficiente", data["error"])
