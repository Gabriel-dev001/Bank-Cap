from app.repository.usuario_repository import UsuarioRepository
from flask_jwt_extended import create_access_token
from datetime import timedelta

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
    
    
