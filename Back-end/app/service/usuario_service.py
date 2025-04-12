from app.repository.usuario_repository import UsuarioRepository

class UsuarioService:
    @staticmethod
    def get_usuarios():
        usuarios = UsuarioRepository.get_usuarios()
        return [usuario.to_dict() for usuario in usuarios]
    
    @staticmethod
    def get_by_id_usuario(usuario_id):
        return UsuarioRepository.get_by_id_usuario(usuario_id)
    
    @staticmethod
    def excluir_usuario(usuario_id):
        usuario = UsuarioRepository.excluir(usuario_id)
        if not usuario:
        
            return {"error": "Usuário não encontrado"}, 404
        
        UsuarioRepository.excluir(usuario)
        return {"message": "Usuário excluído com sucesso"}, 200

