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
            
            nova_conta = Conta(usuario_id=usuario_id, nome=nome, banco=banco, tipo=tipo, saldo=0.00)
            db.session.add(nova_conta)
            db.session.commit()
            return nova_conta.to_dict(), 201
        
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500
        
    @staticmethod
    def listar_todos():
        contas = ContaRepository.listar_todos()
        return [conta.to_dict() for conta in contas]