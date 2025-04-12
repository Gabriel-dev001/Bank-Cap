from app import db
from app.models.receita_model import Receita
from app.repository.receita_repository import ReceitaRepository
from app.service.conta_service import ContaService

class ReceitaService:
    @staticmethod
    def criar_receita(valor, data, categoria, conta_id, descricao=None):
        nova_receita = Receita(
            valor=valor,
            data=data,
            categoria=categoria,
            conta_id=conta_id,
            descricao=descricao
        )

        receita_salva = ReceitaRepository.criar_receita(nova_receita)

        # Altera o saldo da conta após salvar a receita
        ContaService.alterar_saldo(conta_id, float(valor))

        return receita_salva.to_dict(), 201
