from app.models.cripto_model import Cripto
from extensions import db

class CriptoRepository:
    @staticmethod
    def salvar(cripto):
        db.session.add(cripto)
        db.session.commit()
        return cripto

    @staticmethod
    def get_criptos_por_conta(conta_id):
        return Cripto.query.filter_by(conta_id=conta_id).all()

    @staticmethod
    def excluir_cripto(cripto_id):
        cripto = Cripto.query.get(cripto_id)

        if not cripto:
            return None

        valor_reais = cripto.valor_reais
        conta_id = cripto.conta_id

        db.session.delete(cripto)
        db.session.commit()

        return valor_reais, conta_id
