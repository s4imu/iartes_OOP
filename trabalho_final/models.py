import json
from itsdangerous import URLSafeTimedSerializer as Serializer

ARQUIVO_DADOS = "dados.json"
SECRET_KEY = "sua_chave_secreta"


def carregar_dados():
    with open(ARQUIVO_DADOS, "r") as arquivo:
        return json.load(arquivo)


def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)


def gerar_token(usuario):
    s = Serializer(SECRET_KEY)
    return s.dumps({"usuario": usuario})


def validar_token(token):
    s = Serializer(SECRET_KEY)
    try:
        dados = s.loads(token, max_age=3600)
        return dados["usuario"]
    except Exception:
        return None


def autenticar_usuario(usuario, senha):
    dados = carregar_dados()
    usuarios = dados["usuarios"]
    if usuario in usuarios and usuarios[usuario] == senha:
        return gerar_token(usuario)
    return None


def listar_produtos(filtros=None):
    dados = carregar_dados()
    produtos = dados["produtos"]
    if not filtros:
        return produtos
    filtros_validos = {"nome", "categoria"}
    chaves_invalidas = set(filtros.keys()) - filtros_validos
    if chaves_invalidas:
        raise ValueError("Parâmetros de filtro inválidos.")
    nome = filtros.get("nome")
    categoria = filtros.get("categoria")
    produtos_filtrados = [
        produto
        for produto in produtos
        if (not nome or nome.lower() in produto["nome"].lower())
        and (not categoria or categoria.lower() in produto["categoria"].lower())
    ]
    return produtos_filtrados


def criar_produto(dados_produto):
    if dados_produto["quantidade_inicial"] < 0 or dados_produto["preco_unitario"] <= 0:
        raise ValueError("Quantidade ou preço inválidos.")
    dados = carregar_dados()
    produtos = dados["produtos"]
    next_id = max([produto["id"] for produto in produtos], default=0) + 1
    produto = {"id": next_id, **dados_produto}
    produtos.append(produto)
    salvar_dados(dados)
    return produto


def obter_produto_por_id(id):
    dados = carregar_dados()
    produtos = dados["produtos"]
    return next((produto for produto in produtos if produto["id"] == id), None)


def atualizar_produto(id, dados_atualizacao):
    dados = carregar_dados()
    produtos = dados["produtos"]
    produto = obter_produto_por_id(id)
    if not produto:
        return None
    if "nome" in dados_atualizacao and not dados_atualizacao["nome"]:
        raise ValueError("Nome do produto não pode ser vazio.")
    if (
        "preco_unitario" in dados_atualizacao
        and dados_atualizacao["preco_unitario"] <= 0
    ):
        raise ValueError("Preço unitário deve ser maior que zero.")
    produto.update(dados_atualizacao)
    salvar_dados(dados)
    return produto


def entrada_estoque(id, quantidade):
    dados = carregar_dados()
    produtos = dados["produtos"]
    produto = obter_produto_por_id(id)
    if not produto or quantidade < 0:
        raise ValueError("Produto não encontrado ou quantidade inválida.")
    produto["quantidade_inicial"] += quantidade
    salvar_dados(dados)
    return produto


def saida_estoque(id, quantidade):
    dados = carregar_dados()
    produtos = dados["produtos"]
    produto = obter_produto_por_id(id)
    if not produto or quantidade < 0 or produto["quantidade_inicial"] < quantidade:
        raise ValueError("Estoque insuficiente ou dados inválidos.")
    produto["quantidade_inicial"] -= quantidade
    salvar_dados(dados)
    return produto


def remover_produto(id):
    dados = carregar_dados()
    produtos = dados["produtos"]
    produto = obter_produto_por_id(id)
    if not produto:
        return None
    dados["produtos"] = [p for p in produtos if p["id"] != id]
    salvar_dados(dados)
    return produto
