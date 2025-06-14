from flask import Blueprint
from app.controllers.relatorio_controller import RelatorioController

relatorio_bp = Blueprint("relatorio", __name__, url_prefix="/relatorios")

relatorio_bp.route("/conta/<int:conta_id>", methods=["POST"])(RelatorioController.gerar_relatorio)