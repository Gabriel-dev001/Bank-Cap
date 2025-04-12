from flask import Blueprint
from app.controllers.receita_contoller import ReceitaController

receita_bp = Blueprint("receita", __name__, url_prefix="/receitas")

receita_bp.route("/", methods=["POST"])(ReceitaController.criar_receita)
receita_bp.route("/conta/<int:conta_id>", methods=["GET"])(ReceitaController.get_receitas_por_conta)
receita_bp.route("/<int:receita_id>", methods=["GET"])(ReceitaController.get_por_id)
receita_bp.route("/<int:receita_id>", methods=["PUT"])(ReceitaController.editar_receita)
receita_bp.route("/<int:receita_id>", methods=["DELETE"])(ReceitaController.excluir_receita)
