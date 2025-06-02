from app import db
from app.models.receita_model import Receita
from app.repository.receita_repository import ReceitaRepository
from app.service.conta_service import ContaService
from decimal import Decimal
from sqlalchemy.orm import joinedload

from app.service.log_service import LogService

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
        ContaService.alterar_saldo(conta_id, float(valor))
        
        LogService.salvar_log(conta_id, f"Receita na conta id: {conta_id} Criada")

        return receita_salva.to_dict(), 201
    
    @staticmethod
    def get_receitas_por_conta(conta_id):
        receitas = ReceitaRepository.get_receitas_por_conta(conta_id)

        if not receitas:
            return {"message": "Nenhuma receita encontrada para esta conta"}, 404

        return [r.to_dict() for r in receitas], 200
    
    @staticmethod
    def get_por_id(receita_id):
        receita = ReceitaRepository.get_por_id(receita_id)

        if receita is None:
            return {"mensagem": "Receita não encontrada"}, 404

        return receita.to_dict(), 200
    
    @staticmethod
    def editar_receita(receita_id, novo_valor, nova_data, nova_categoria, nova_descricao):
        receita = Receita.query.options(joinedload(Receita.conta)).filter_by(id=receita_id).first()
        
        if not receita:
            return None, 404

        diferenca_valor = Decimal(novo_valor) - Decimal(str(receita.valor))

        receita_editada = ReceitaRepository.editar_receita(receita_id, {
        "valor": novo_valor,
        "data": nova_data,
        "categoria": nova_categoria,
        "descricao": nova_descricao
        })
        
        conta_id = receita.conta.id  
        ContaService.alterar_saldo(conta_id, diferenca_valor)
        
        LogService.salvar_log(conta_id, f"Receita id: {receita_id} editada")

        return receita_editada.to_dict(), 200

    @staticmethod
    def excluir_receita(receita_id):
        result = ReceitaRepository.excluir_receita(receita_id)

        if result is None:
            return {"error": "Receita não encontrada"}, 404

        valor, conta_id = result
        ContaService.alterar_saldo(conta_id, -Decimal(valor))
        
        LogService.salvar_log(conta_id, f"Receita id: {receita_id} excluida")
        
        return {"message": "Receita excluída com sucesso"}, 200
