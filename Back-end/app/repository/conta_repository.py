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