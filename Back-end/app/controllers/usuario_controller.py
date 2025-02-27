from flask import Blueprint, jsonify
from app.service.usuario_service import UsuarioService

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuarios')

@usuario_bp.route('/', methods=['GET'])
def listar_usuarios():
    usuarios = UsuarioService.listar_todos()
    return jsonify(usuarios), 200

@staticmethod
def excluir_usuario(usuario_id):
    resposta, status_code = UsuarioService.excluir_usuario(usuario_id)
    return jsonify(resposta), status_code
