from flask import Blueprint
from app.controllers.despesa_controller import DespesaController

despesa_bp = Blueprint("despesa", __name__, url_prefix="/despesas")

despesa_bp.route("/", methods=["POST"])(DespesaController.criar_despesa)
despesa_bp.route("/conta/<int:conta_id>", methods=["GET"])(DespesaController.get_despesas_por_conta)
despesa_bp.route("/<int:depesa_id>", methods=["GET"])(DespesaController.get_por_id)
despesa_bp.route("/<int:depesa_id>", methods=["PUT"])(DespesaController.editar_despesa)
despesa_bp.route("/<int:depesa_id>", methods=["DELETE"])(DespesaController.excluir_despesa)
