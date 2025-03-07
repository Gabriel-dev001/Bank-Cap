from flask import request, jsonify, redirect
from app.service.auth_service import AuthService

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
            return jsonify({"error": "Dados incompletos"}), 400

        return AuthService.registrar_usuario(data["nome"], data["email"], data["senha"])
    
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

    
    