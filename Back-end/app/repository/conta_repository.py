from app.models.conta_model import Conta
from extensions import db

class ContaRepository:
    @staticmethod
    def criar_conta(nome, banco, tipo, saldo):
        nova_conta = Conta(nome=nome, banco=banco, tipo=tipo, saldo=saldo)
        db.session.add(nova_conta)
        db.session.commit()
        return nova_conta
    
    @staticmethod
    def listar_todos():
        return Conta.query.all()
    
    @staticmethod
    def buscar_por_id(conta_id):
        return Conta.query.get(conta_id)

    @staticmethod
    def atualizar(conta):
        db.session.commit()
    
    @staticmethod
    def deletar(conta):
        db.session.delete(conta)
        db.session.commit()