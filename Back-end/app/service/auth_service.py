import os
import requests
from urllib.parse import urlencode
from app.repository.usuario_repository import UsuarioRepository
from flask_jwt_extended import create_access_token
from datetime import timedelta

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")

GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v1/userinfo"

class AuthService:
    @staticmethod
    def registrar_usuario(nome, email, senha):
        if UsuarioRepository.buscar_por_email(email):
            return {"error": "Email já cadastrado"}, 400

        usuario = UsuarioRepository.criar_usuario(nome, email, senha)
        return {"id_usuario": usuario.id, "usuario": usuario.to_dict()}, 201

    @staticmethod
    def login(email, senha):
        usuario = UsuarioRepository.buscar_por_email(email)
        if not usuario or not usuario.verificar_senha(senha):
            return {"error": "Credenciais inválidas"}, 401

        token = create_access_token(identity={"id": usuario.id, "email": usuario.email}, expires_delta=timedelta(hours=1))
        return {"id_usuario": usuario.id, "token": token}, 200
    
    #Continuar com Google:
    @staticmethod
    def login_com_google(google_id, email):
        usuario = UsuarioRepository.buscar_por_google_id(google_id)
        if not usuario:
            return {"error": "Usuário não encontrado"}, 404

        token = create_access_token(identity={"id": usuario.id, "email": usuario.email}, expires_delta=timedelta(hours=1))
        return {"id_usuario": usuario.id, "token": token}, 200
    
    @staticmethod
    def registrar_usuario_google(nome, email, google_id):
        if UsuarioRepository.buscar_por_email(email):
            return {"error": "Email já cadastrado"}, 400

        usuario = UsuarioRepository.criar_usuario_google(nome, email, google_id)
        return {"id_usuario": usuario.id, "usuario": usuario.to_dict()}, 201
