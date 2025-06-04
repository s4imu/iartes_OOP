from faker import Faker
import unittest
import json
from app import app
from models import gerar_relatorio_testes_csv, gerar_relatorio_produtos_csv


class TestEstoque(unittest.TestCase):
    resultados_testes = []

    def setUp(self):
        self.client = app.test_client()
        self.headers = {"Content-Type": "application/json"}
        self.fake = Faker("pt_BR")
        self.token = self.obter_token_autorizacao()
        self.headers["Authorization"] = self.token

    def tearDown(self):
        resultado = {
            "teste": self._testMethodName,
            "resultado": "sucesso" if self._outcome.success else "falha",
            "mensagem": (
                str(self._outcome.errors[-1][1]) if self._outcome.errors else ""
            ),
        }
        self.resultados_testes.append(resultado)

    @classmethod
    def tearDownClass(cls):
        gerar_relatorio_testes_csv(resultados=cls.resultados_testes)
        gerar_relatorio_produtos_csv(nome_arquivo="relatorio_produtos.csv")

    def obter_token_autorizacao(self):
        credenciais = {"usuario": "admin", "senha": "senha123"}
        response = self.client.post(
            "/login", data=json.dumps(credenciais), headers=self.headers
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        return data["token"]

    def gerar_produto_ficticio(self):
        return {
            "nome": self.fake.word(),
            "categoria": self.fake.word(),
            "quantidade_inicial": self.fake.random_int(min=0, max=100),
            "preco_unitario": self.fake.random_int(min=1, max=10000) / 100,
        }

    # Cenários de Sucesso
    def test_CT001_criar_produto_valido(self):
        produto = self.gerar_produto_ficticio()
        response = self.client.post(
            "/produtos", data=json.dumps(produto), headers=self.headers
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data["nome"], produto["nome"])

    def test_CT002_listar_produtos(self):
        response = self.client.get("/produtos", headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_CT003_buscar_produto(self):
        produto = self.gerar_produto_ficticio()
        response_criacao = self.client.post(
            "/produtos", data=json.dumps(produto), headers=self.headers
        )
        self.assertEqual(response_criacao.status_code, 201)
        dados_criacao = json.loads(response_criacao.data)
        produto_id = dados_criacao["id"]

        response_busca = self.client.get(
            f"/produtos/{produto_id}", headers=self.headers
        )
        self.assertEqual(response_busca.status_code, 200)
        dados_busca = json.loads(response_busca.data)
        self.assertEqual(dados_busca["nome"], produto["nome"])

    def test_CT004_buscar_produtos_com_filtro(self):
        produto1 = self.gerar_produto_ficticio()
        produto2 = self.gerar_produto_ficticio()
        self.client.post("/produtos", data=json.dumps(produto1), headers=self.headers)
        self.client.post("/produtos", data=json.dumps(produto2), headers=self.headers)
        response = self.client.get(
            f"/produtos?categoria={produto1['categoria']}", headers=self.headers
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        for produto in data:
            self.assertEqual(produto["categoria"], produto1["categoria"])

    def test_CT005_atualizar_produto(self):
        produto = self.gerar_produto_ficticio()
        response_criacao = self.client.post(
            "/produtos", data=json.dumps(produto), headers=self.headers
        )
        data_criacao = json.loads(response_criacao.data)
        produto_id = data_criacao["id"]
        atualizacao = {
            "nome": self.fake.word(),
            "preco_unitario": self.fake.random_int(min=1, max=10000) / 100,
        }
        response = self.client.put(
            f"/produtos/{produto_id}",
            data=json.dumps(atualizacao),
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["nome"], atualizacao["nome"])

    def test_CT006_entrada_estoque(self):
        produto = self.gerar_produto_ficticio()
        response_criacao = self.client.post(
            "/produtos", data=json.dumps(produto), headers=self.headers
        )
        data_criacao = json.loads(response_criacao.data)
        produto_id = data_criacao["id"]
        quantidade = self.fake.random_int(min=1, max=50)
        response = self.client.post(
            f"/produtos/{produto_id}/entrada",
            data=json.dumps({"quantidade": quantidade}),
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(
            data["quantidade_inicial"], produto["quantidade_inicial"] + quantidade
        )

    def test_CT007_saida_estoque(self):
        produto = self.gerar_produto_ficticio()
        response_criacao = self.client.post(
            "/produtos", data=json.dumps(produto), headers=self.headers
        )
        self.assertEqual(response_criacao.status_code, 201)
        dados_apos_criacao = json.loads(response_criacao.data)
        produto_id = dados_apos_criacao["id"]

        quantidade = self.fake.random_int(min=1, max=produto["quantidade_inicial"])
        response_saida = self.client.post(
            f"/produtos/{produto_id}/saida",
            data=json.dumps({"quantidade": quantidade}),
            headers=self.headers,
        )
        self.assertEqual(response_saida.status_code, 200)
        dados_apos_saida = json.loads(response_saida.data)
        self.assertEqual(
            dados_apos_saida["quantidade_inicial"],
            produto["quantidade_inicial"] - quantidade,
        )

    def test_CT008_remover_produto(self):
        produto = self.gerar_produto_ficticio()
        reponse_criacao = self.client.post(
            "/produtos", data=json.dumps(produto), headers=self.headers
        )
        data = json.loads(reponse_criacao.data)
        produto_id = data["id"]
        response = self.client.delete(f"/produtos/{produto_id}", headers=self.headers)
        self.assertEqual(response.status_code, 200)

    # Cenários de Erro de Validação
    def test_CT009_cadastrar_produto_sem_dados(self):
        response = self.client.post("/produtos", headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_CT010_criar_produto_invalido(self):
        produto = self.gerar_produto_ficticio()
        produto["quantidade_inicial"] = -5
        response = self.client.post(
            "/produtos", data=json.dumps(produto), headers=self.headers
        )
        self.assertEqual(response.status_code, 400)

    def test_CT011_entrada_estoque_invalida(self):
        produto = self.gerar_produto_ficticio()
        self.client.post("/produtos", data=json.dumps(produto), headers=self.headers)
        response = self.client.post(
            "/produtos/1/entrada",
            data=json.dumps({"quantidade": -5}),
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        erro_msg = "Quantidade inválida"
        self.assertIn(erro_msg.lower(), data["error"])

    def test_CT012_atualizar_produto_com_dados_invalidos(self):
        produto = self.gerar_produto_ficticio()
        response_criacao = self.client.post(
            "/produtos", data=json.dumps(produto), headers=self.headers
        )
        dados_apos_criacao = json.loads(response_criacao.data)
        produto_id = dados_apos_criacao["id"]

        atualizacao = {"nome": "", "preco_unitario": -3000.00}
        response = self.client.put(
            f"/produtos/{produto_id}",
            data=json.dumps(atualizacao),
            headers=self.headers,
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
        atualizacao = {
            "nome": self.fake.word(),
            "preco_unitario": self.fake.random_int(min=1, max=10000) / 100,
        }
        response = self.client.put(
            "/produtos/999", data=json.dumps(atualizacao), headers=self.headers
        )
        self.assertEqual(response.status_code, 404)

    def test_CT017_remover_produto_inexistente(self):
        response = self.client.delete("/produtos/999", headers=self.headers)
        self.assertEqual(response.status_code, 404)

    # Cenários de Operações com Estoque Zerado ou Negativo
    def test_CT018_saida_estoque_insuficiente(self):
        produto = self.gerar_produto_ficticio()
        produto["quantidade_inicial"] = 5
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
        produto = self.gerar_produto_ficticio()
        produto["quantidade_inicial"] = 0
        self.client.post("/produtos", data=json.dumps(produto), headers=self.headers)
        response = self.client.post(
            "/produtos/1/saida",
            data=json.dumps({"quantidade": 5}),
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn("Estoque insuficiente", data["error"])
