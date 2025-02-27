from flask import Blueprint, jsonify
from app.service.usuario_service import UsuarioService

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuarios')

@usuario_bp.route('/', methods=['GET'])
def get_usuarios():
    usuarios = UsuarioService.listar_todos()
    return jsonify(usuarios), 200

@usuario_bp.route("/<int:usuario_id>", methods=["DELETE"])
def excluir_usuario(usuario_id):
    return jsonify(UsuarioService.excluir_usuario(usuario_id))