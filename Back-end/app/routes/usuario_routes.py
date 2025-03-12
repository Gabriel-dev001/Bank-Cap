from flask import Blueprint
from app.controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint("usuario", __name__, url_prefix="/usuarios")

usuario_bp.route("/", methods=["GET"])(UsuarioController.listar_todos)
usuario_bp.route("/<int:usuario_id>", methods=["DELETE"])(UsuarioController.excluir_usuario)
