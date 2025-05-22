from flask import request, jsonify, Response
import json
from app.service.auth_service import AuthService
from flask_jwt_extended import jwt_required, get_jwt_identity


class AuthController:
    @staticmethod
    def login():
        data = request.get_json()
        if not all(key in data for key in ("email", "senha")):
            return jsonify({"error": "Dados incompletos"}), 400

        return AuthService.login(data["email"], data["senha"])

    @staticmethod
    def registrar():
        data = request.get_json()
        if not all(key in data for key in ("nome", "email", "senha")):
            return Response(json.dumps({"error": "Dados incompletos"}, ensure_ascii=False), 
                            status=400, mimetype="application/json")

        usuario, status_code = AuthService.registrar_usuario(data["nome"], data["email"], data["senha"])

        if "error" in usuario:
            return Response(json.dumps({"error": usuario["error"]}, ensure_ascii=False), 
                            status=status_code, mimetype="application/json")

        return Response(json.dumps(usuario["usuario"], ensure_ascii=False), 
                        status=status_code, mimetype="application/json")
        
        
    @staticmethod
    # @jwt_required()
    def trocar_senha(usuario_id):
        data = request.get_json()

        if not all(key in data for key in ("senha_atual", "nova_senha")):
            return jsonify({"error": "Dados incompletos"}), 400

        return AuthService.trocar_senha(usuario_id, data["senha_atual"], data["nova_senha"])
    
    @staticmethod
    def login_com_google():
        data = request.get_json()
        
        if not all(key in data for key in ("email", "google_id")):
            return jsonify({"error": "Dados incompletos"}), 400

        return AuthService.login_com_google(data["google_id"], data["email"])
    
    @staticmethod
    def registrar_com_google():
        data = request.get_json()
        
        if not all(key in data for key in ("nome", "email", "google_id")):
            return jsonify({"error": "Dados incompletos"}), 400

        return AuthService.registrar_usuario_google(data["nome"], data["email"], data["google_id"])

    @staticmethod
    def callback_google():
        # Aqui você pode implementar a lógica para lidar com o callback do Google, se necessário
        return jsonify({"message": "Google login callback"})

    
    