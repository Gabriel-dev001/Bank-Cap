from app.models.conta_model import Conta
from extensions import db
from decimal import Decimal


class ContaRepository:
    @staticmethod
    def criar_conta(nova_conta):
        db.session.add(nova_conta)
        db.session.commit()
        return nova_conta
    
    @staticmethod
    def get_contas():
        return Conta.query.all()
    
    @staticmethod
    def get_by_id_conta(conta_id):
        return Conta.query.get(conta_id)
    
    @staticmethod
    def get_contas_usuario(usuario_id):
        return Conta.query.filter_by(usuario_id=usuario_id).all()

    @staticmethod
    def atualizar(conta):
        db.session.commit()
    
    @staticmethod
    def deletar(conta):
        db.session.delete(conta)
        db.session.commit()

    @staticmethod
    def alterar_saldo(conta_id, valor):
        conta = Conta.query.get(conta_id)
        if not conta:
            return False

        conta.saldo += Decimal(valor)  
        db.session.commit()
        return True