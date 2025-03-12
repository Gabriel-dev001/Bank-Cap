from flask import request, jsonify
from app.service.usuario_service import UsuarioService

class UsuarioController:
    @staticmethod
    def listar_todos():
        usuarios = UsuarioService.listar_todos()
        return jsonify(usuarios), 200

    @staticmethod
    def excluir_usuario(usuario_id):
        resposta, status_code = UsuarioService.excluir_usuario(usuario_id)
        return jsonify(resposta), status_code
