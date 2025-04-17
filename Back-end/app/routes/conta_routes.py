from flask import Blueprint, jsonify
from app.controllers.conta_controller import ContaController

conta_bp = Blueprint("conta", __name__, url_prefix="/contas")

conta_bp.route("/", methods=["GET"])(ContaController.get_contas)
conta_bp.route("/usuario/<int:usuario_id>", methods=["GET"])(ContaController.get_contas_usuario)
conta_bp.route("/<int:conta_id>", methods=["GET"])(ContaController.get_by_id_contas)
conta_bp.route("/", methods=["POST"])(ContaController.criar_conta)
conta_bp.route("/<int:conta_id>", methods=["PUT"])(ContaController.editar_conta)
conta_bp.route("/<int:conta_id>", methods=["DELETE"])(ContaController.deletar_conta)

