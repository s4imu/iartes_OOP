from itsdangerous import URLSafeTimedSerializer as Serializer

usuarios = {"admin": "senha123"}
SECRET_KEY = "sua_chave_secreta"
produtos = []
next_id = 1


def gerar_token(usuario):
    s = Serializer(SECRET_KEY)
    return s.dumps({"usuario": usuario})


def validar_token(token):
    s = Serializer(SECRET_KEY)
    try:
        dados = s.loads(token, max_age=3600)  # Define o tempo de expiração aqui
        return dados["usuario"]
    except Exception:
        return None


def autenticar_usuario(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        return gerar_token(usuario)
    return None


def listar_produtos(filtros=None):
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


def criar_produto(dados):
    global next_id
    if dados["quantidade_inicial"] < 0 or dados["preco_unitario"] <= 0:
        raise ValueError("Quantidade ou preço inválidos.")
    produto = {"id": next_id, **dados}
    produtos.append(produto)
    next_id += 1
    return produto


def obter_produto_por_id(id):
    return next((produto for produto in produtos if produto["id"] == id), None)


def atualizar_produto(id, dados):
    produto = obter_produto_por_id(id)
    if not produto:
        return None
    if "nome" in dados and not dados["nome"]:
        raise ValueError("Nome do produto não pode ser vazio.")
    if "preco_unitario" in dados and dados["preco_unitario"] <= 0:
        raise ValueError("Preço unitário deve ser maior que zero.")
    produto.update(dados)
    return produto


def entrada_estoque(id, quantidade):
    produto = obter_produto_por_id(id)
    if not produto or quantidade < 0:
        raise ValueError("Produto não encontrado ou quantidade inválida.")
    produto["quantidade_inicial"] += quantidade
    return produto


def saida_estoque(id, quantidade):
    produto = obter_produto_por_id(id)
    if not produto or quantidade < 0 or produto["quantidade_inicial"] < quantidade:
        raise ValueError("Estoque insuficiente ou dados inválidos.")
    produto["quantidade_inicial"] -= quantidade
    return produto


def remover_produto(id):
    global produtos
    produto = obter_produto_por_id(id)
    if not produto:
        return None
    produtos = [p for p in produtos if p["id"] != id]
    return produto
