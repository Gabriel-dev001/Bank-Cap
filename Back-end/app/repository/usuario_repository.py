from app.models.usuario_model import Usuario
from extensions import db

class UsuarioRepository:

    @staticmethod
    def criar_usuario(nome, email, senha):
        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()
        return novo_usuario
    
    @staticmethod
    def criar_usuario_google(nome, email, google_id):
        usuario = Usuario(nome=nome, email=email, google_id=google_id)
        db.session.add(usuario)
        db.session.commit()
        return usuario

    @staticmethod
    def buscar_por_email(email):
        return Usuario.query.filter_by(email=email).first()
    
    @staticmethod
    def buscar_por_google_id(google_id):
        return Usuario.query.filter_by(google_id=google_id).first()
        
    
    @staticmethod
    def listar_todos():
        return Usuario.query.all()
    
    @staticmethod
    def buscar_por_id(usuario_id):
        return Usuario.query.get(usuario_id)

    @staticmethod
    def excluir(usuario):
        db.session.delete(usuario)
        db.session.commit()
