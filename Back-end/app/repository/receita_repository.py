from app.models.receita_model import Receita
from extensions import db


class ReceitaRepository:
    @staticmethod
    def criar_receita(nova_receita):
        db.session.add(nova_receita)
        db.session.commit()
        return nova_receita
