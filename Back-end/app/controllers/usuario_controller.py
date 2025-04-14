from flask import request, jsonify, Response
import json
from app.service.usuario_service import UsuarioService

class UsuarioController:
    @staticmethod
    def get_usuarios():
        usuarios = UsuarioService.get_usuarios()
        
        return Response(json.dumps(usuarios, ensure_ascii=False), status=200, mimetype="application/json")
    
    @staticmethod
    def get_by_id_usuario(usuario_id):
        usuario = UsuarioService.get_by_id_usuario(usuario_id)

        if usuario:
            return Response(json.dumps(usuario.to_dict(), ensure_ascii=False), status=200, mimetype="application/json")
            
        return Response(json.dumps({"erro": "Usuário não encontrado"}), status=404, mimetype="application/json")

    
    @staticmethod
    def editar_usuario(usuario_id):
        data = request.get_json()
        nome = data.get('nome')
        email = data.get('email')
        senha = data.get('senha')

        usuario_editado, status = UsuarioService.editar_usuario(
            usuario_id=usuario_id,
            nome=nome,
            email=email,
            senha=senha
        )
    
        return Response(json.dumps(usuario_editado, ensure_ascii=False),status=status,mimetype="application/json")  
    
    @staticmethod
    def excluir_usuario(usuario_id):
        resposta, status_code = UsuarioService.excluir_usuario(usuario_id)
        return jsonify(resposta), status_code
