from app import db
from app.repository.conta_repository import ContaRepository
from app.models.conta_model import Conta
from app.models.usuario_model import Usuario
from app.repository.usuario_repository import UsuarioRepository


class ContaService:
    @staticmethod
    def criar_conta(usuario_id, nome, banco, tipo):
        try:
            usuario = Usuario.query.get(usuario_id)
            if not usuario:
                return {"error": "Usuário não encontrado"}, 404

            nova_conta = Conta(
                usuario_id=usuario_id,
                nome=nome,
                banco=banco,
                tipo=tipo,
                saldo=0.00
            )
            
            conta_criada = ContaRepository.criar_conta(nova_conta)
            return conta_criada.to_dict(), 201

        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500
        
    @staticmethod
    def get_contas():
        contas = ContaRepository.get_contas()
        return [conta.to_dict() for conta in contas]
    
    @staticmethod
    def get_by_id_conta(conta_id):
        return ContaRepository.get_by_id_conta(conta_id)
    
    @staticmethod
    def editar_conta(conta_id, data):
        # Buscar a conta pelo ID
        conta = ContaRepository.get_by_id_conta(conta_id)
        if not conta:
            return {"error": "Conta não encontrada"}, 404

        # Buscar o usuário pelo ID fornecido no JSON
        usuario_id = data.get("usuario_id")
        usuario = Usuario.query.get(usuario_id)
        if not usuario:
            return {"error": "Usuário não encontrado"}, 404

        # Atualizar os campos da conta
        for key, value in data.items():
            if key in ["usuario_id", "nome", "banco", "tipo"] and hasattr(conta, key):
                setattr(conta, key, value)

        # Salvar alterações
        ContaRepository.atualizar(conta)
        
        return conta.to_dict(), 200
    
    @staticmethod
    def deletar_conta(conta_id):
        conta = ContaRepository.get_by_id_conta(conta_id)
        if not conta:
            return {"error": "Conta não encontrada"}, 404

        ContaRepository.deletar(conta)
        return {"message": "Conta deletada com sucesso"}, 200