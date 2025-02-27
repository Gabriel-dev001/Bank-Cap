from flask import request, jsonify
from app.service.auth_service import AuthService

class AuthController:
    @staticmethod
    def registrar():
        data = request.get_json()
        if not all(key in data for key in ("nome", "email", "senha")):
            return jsonify({"error": "Dados incompletos"}), 400

        return AuthService.registrar_usuario(data["nome"], data["email"], data["senha"])

    @staticmethod
    def login():
        data = request.get_json()
        if not all(key in data for key in ("email", "senha")):
            return jsonify({"error": "Dados incompletos"}), 400

        return AuthService.login(data["email"], data["senha"])
