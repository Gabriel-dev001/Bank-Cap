from flask import request, jsonify, Response
import json
from app.service.usuario_service import UsuarioService

class UsuarioController:
    @staticmethod
    def listar_todos():
        usuarios = UsuarioService.listar_todos()
        
        return Response(json.dumps(usuarios, ensure_ascii=False), 
                    status=200, mimetype="application/json")

    @staticmethod
    def excluir_usuario(usuario_id):
        resposta, status_code = UsuarioService.excluir_usuario(usuario_id)
        return jsonify(resposta), status_code
