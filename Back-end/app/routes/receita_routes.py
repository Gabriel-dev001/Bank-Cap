from flask import Blueprint
from app.controllers.receita_contoller import ReceitaController

receita_bp = Blueprint("receita", __name__, url_prefix="/receitas")

receita_bp.route("/", methods=["POST"])(ReceitaController.criar_receita)
