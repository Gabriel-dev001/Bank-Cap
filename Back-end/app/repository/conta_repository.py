from app.models.conta_model import Conta
from extensions import db

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
    def atualizar(conta):
        db.session.commit()
    
    @staticmethod
    def deletar(conta):
        db.session.delete(conta)
        db.session.commit()