from app.models.receita_model import Receita
from extensions import db


class ReceitaRepository:
    @staticmethod
    def criar_receita(nova_receita):
        db.session.add(nova_receita)
        db.session.commit()
        return nova_receita
    
    @staticmethod
    def get_receitas_por_conta(conta_id):
        receitas = Receita.query.filter_by(conta_id=conta_id).all()
        return receitas
    
    @staticmethod
    def get_por_id(receita_id):
        return Receita.query.filter_by(id=receita_id).join(Receita.conta).first()
    
    @staticmethod
    def editar_receita(receita_id, novos_dados):
        receita = Receita.query.get(receita_id)
        if not receita:
            return None

        for chave, valor in novos_dados.items():
            if hasattr(receita, chave):
                setattr(receita, chave, valor)

        db.session.commit()
        return receita
    
    @staticmethod
    def excluir_receita(receita_id):
        receita = Receita.query.get(receita_id)

        if not receita:
            return None  

        valor = receita.valor
        conta_id = receita.conta_id

        db.session.delete(receita)
        db.session.commit()

        return valor, conta_id 
