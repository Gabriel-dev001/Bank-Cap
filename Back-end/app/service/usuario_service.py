from app.repository.usuario_repository import UsuarioRepository
from werkzeug.security import generate_password_hash

class UsuarioService:
    @staticmethod
    def get_usuarios():
        usuarios = UsuarioRepository.get_usuarios()
        return [usuario.to_dict() for usuario in usuarios]
    
    @staticmethod
    def get_by_id_usuario(usuario_id):
        return UsuarioRepository.get_by_id_usuario(usuario_id)
    
    
    @staticmethod
    def editar_usuario(usuario_id, nome=None, email=None, senha=None):
        usuario = UsuarioRepository.get_by_id_usuario(usuario_id)
        if not usuario:
            return {"message": "Usuário não encontrado"}, 404

        dados_atualizados = {}
        if nome:
            dados_atualizados["nome"] = nome
        if email:
            dados_atualizados["email"] = email
        if senha:
            dados_atualizados["senha"] = generate_password_hash(senha)

        usuario_atualizado = UsuarioRepository.editar_usuario(usuario_id, dados_atualizados)
        return usuario_atualizado.to_dict(), 200
    
    @staticmethod
    def excluir_usuario(usuario_id):
        usuario = UsuarioRepository.get_by_id_usuario(usuario_id)
        if not usuario:
            return {"error": "Usuário não encontrado"}, 404
    
        UsuarioRepository.excluir(usuario) 
        return {"message": "Usuário excluído com sucesso"}, 200