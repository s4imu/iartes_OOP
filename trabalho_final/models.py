produtos = []
next_id = 1


def listar_produtos(filtros=None):
    if filtros:
        nome = filtros.get("nome")
        categoria = filtros.get("categoria")
        return [
            produto
            for produto in produtos
            if (not nome or nome.lower() in produto["nome"].lower())
            and (not categoria or categoria.lower() == produto["categoria"].lower())
        ]
    return produtos


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
