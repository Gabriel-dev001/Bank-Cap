from flask import Blueprint
from app.controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint("usuario", __name__, url_prefix="/usuarios")

usuario_bp.route("/", methods=["GET"])(UsuarioController.get_usuarios)
usuario_bp.route("/<int:usuario_id>", methods=["GET"])(UsuarioController.get_by_id_usuario)
usuario_bp.route("/<int:usuario_id>", methods=["DELETE"])(UsuarioController.excluir_usuario)
