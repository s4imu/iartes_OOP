from flask import Blueprint, jsonify, request
from models import (
    listar_produtos,
    criar_produto,
    obter_produto_por_id,
    atualizar_produto,
    entrada_estoque,
    saida_estoque,
    remover_produto,
)

inventario_routes = Blueprint("inventario", __name__)


@inventario_routes.route("/produtos", methods=["GET"])
def rota_listar_produtos():
    filtros = request.args
    try:
        produtos_filtrados = listar_produtos(filtros)
        if not produtos_filtrados:
            return jsonify({"error": "Nenhum produto encontrado"}), 404
        return jsonify(produtos_filtrados), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@inventario_routes.route("/produtos", methods=["POST"])
def rota_criar_produto():
    dados = request.get_json()
    try:
        produto = criar_produto(dados)
        return jsonify(produto), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@inventario_routes.route("/produtos/<int:id>", methods=["GET"])
def rota_obter_produto(id):
    produto = obter_produto_por_id(id)
    if not produto:
        return jsonify({"error": "Produto não encontrado"}), 404
    return jsonify(produto), 200


@inventario_routes.route("/produtos/<int:id>", methods=["PUT"])
def rota_atualizar_produto(id):
    dados = request.get_json()
    try:
        produto = atualizar_produto(id, dados)
        if not produto:
            return jsonify({"error": "Produto não encontrado"}), 404
        return jsonify(produto), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@inventario_routes.route("/produtos/<int:id>/entrada", methods=["POST"])
def rota_entrada_estoque(id):
    dados = request.get_json()
    try:
        produto = entrada_estoque(id, dados["quantidade"])
        return jsonify(produto), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@inventario_routes.route("/produtos/<int:id>/saida", methods=["POST"])
def rota_saida_estoque(id):
    dados = request.get_json()
    try:
        produto = saida_estoque(id, dados["quantidade"])
        return jsonify(produto), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@inventario_routes.route("/produtos/<int:id>", methods=["DELETE"])
def rota_remover_produto(id):
    produto = remover_produto(id)
    if not produto:
        return jsonify({"error": "Produto não encontrado"}), 404
    return jsonify(produto), 200
