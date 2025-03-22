from flask import Blueprint, jsonify
from app.controllers.conta_controller import ContaController

conta_bp = Blueprint("conta", __name__, url_prefix="/contas")

conta_bp.route("/", methods=["GET"])(ContaController.listar_contas)
conta_bp.route("/create", methods=["POST"])(ContaController.criar_conta)
conta_bp.route("/edit/<int:conta_id>", methods=["PUT"])(ContaController.editar_conta)
conta_bp.route("/delete/<int:conta_id>", methods=["DELETE"])(ContaController.deletar_conta)

