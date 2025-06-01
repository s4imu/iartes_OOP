produtos = []
next_id = 1


def listar_produtos():
    return produtos


def criar_produto(dados):
    global next_id
    produto = {"id": next_id, **dados}
    produtos.append(produto)
    next_id += 1
    return produto
