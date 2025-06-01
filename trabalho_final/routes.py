from flask import Blueprint, jsonify, request
from models import listar_produtos, criar_produto

inventario_routes = Blueprint("inventario", __name__)


@inventario_routes.route("/produtos", methods=["GET"])
def rota_listar_produtos():
    return jsonify(listar_produtos()), 200


@inventario_routes.route("/produtos", methods=["POST"])
def rota_criar_produto():
    dados = request.get_json()
    return jsonify(criar_produto(dados)), 201
