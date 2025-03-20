from app.repository.usuario_repository import UsuarioRepository

class UsuarioService:
    @staticmethod
    def listar_todos():
        usuarios = UsuarioRepository.listar_todos()
        return [usuario.to_dict() for usuario in usuarios]
    
    @staticmethod
    def excluir_usuario(usuario_id):
        usuario = UsuarioRepository.buscar_por_id(usuario_id)
        if not usuario:
        
            return {"error": "Usuário não encontrado"}, 404
        
        UsuarioRepository.excluir(usuario)
        return {"message": "Usuário excluído com sucesso"}, 200

