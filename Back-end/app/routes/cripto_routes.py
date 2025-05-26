from flask import Blueprint
from app.controllers.cripto_controller import CriptoController

cripto_bp = Blueprint("cripto", __name__, url_prefix="/cripto")

cripto_bp.route("/", methods=["POST"])(CriptoController.criar_cripto)
cripto_bp.route("/conta/<int:conta_id>", methods=["GET"])(CriptoController.get_criptos_por_conta)
cripto_bp.route("/<int:cripto_id>", methods=["DELETE"])(CriptoController.excluir_cripto)
