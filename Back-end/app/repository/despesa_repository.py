from app.models.despesa_model import Despesa
from extensions import db


class DespesaRepository:
    @staticmethod
    def criar_despesa(nova_despesa):
        db.session.add(nova_despesa)
        db.session.commit()
        return nova_despesa
    
    @staticmethod
    def get_despesas_por_conta(conta_id):
        despesas = Despesa.query.filter_by(conta_id=conta_id).all()
        return despesas
    
    @staticmethod
    def get_por_id(despesa_id):
        return Despesa.query.filter_by(id=despesa_id).join(Despesa.conta).first()
    
    @staticmethod
    def editar_despesa(despesa_id, novos_dados):
        despesa = Despesa.query.get(despesa_id)
        if not despesa:
            return None

        for chave, valor in novos_dados.items():
            if hasattr(despesa, chave):
                setattr(despesa, chave, valor)

        db.session.commit()
        return despesa
    
    @staticmethod
    def excluir_despesa(despesa_id):
        despesa = Despesa.query.get(despesa_id)

        if not despesa:
            return None  

        valor = despesa.valor
        conta_id = despesa.conta_id

        db.session.delete(despesa)
        db.session.commit()

        return valor, conta_id 
