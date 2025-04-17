from app import db
from app.repository.conta_repository import ContaRepository
from app.models.conta_model import Conta
from app.models.usuario_model import Usuario

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
    def get_contas_usuario(usuario_id):
        contas = ContaRepository.get_contas_usuario(usuario_id)
        if not contas:
            return {"message": "Nenhuma conta encontrada para este usuário"}, 404
        
        return [conta.to_dict() for conta in contas], 200
    
    @staticmethod
    def editar_conta(conta_id, data):
        conta = ContaRepository.get_by_id_conta(conta_id)
        if not conta:
            return {"error": "Conta não encontrada"}, 404

        usuario_id = data.get("usuario_id")
        usuario = Usuario.query.get(usuario_id)
        if not usuario:
            return {"error": "Usuário não encontrado"}, 404

        for key, value in data.items():
            if key in ["usuario_id", "nome", "banco", "tipo"] and hasattr(conta, key):
                setattr(conta, key, value)

        ContaRepository.atualizar(conta)
        
        return conta.to_dict(), 200
    
    @staticmethod
    def deletar_conta(conta_id):
        conta = ContaRepository.get_by_id_conta(conta_id)
        if not conta:
            return {"error": "Conta não encontrada"}, 404

        ContaRepository.deletar(conta)
        return {"message": "Conta deletada com sucesso"}, 200
    
    @staticmethod
    def alterar_saldo(conta_id, valor):
        return ContaRepository.alterar_saldo(conta_id, valor)
