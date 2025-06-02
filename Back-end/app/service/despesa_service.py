from app import db
from app.models.despesa_model import Despesa
from app.repository.despesa_repository import DespesaRepository
from app.service.conta_service import ContaService
from decimal import Decimal
from sqlalchemy.orm import joinedload

from app.service.log_service import LogService


class DespesaService:
    @staticmethod
    def criar_despesa(valor, data, categoria, conta_id, descricao=None):
        valor = -abs(float(valor))
        print(valor)
        
        nova_despesa = Despesa(
            valor=valor,
            data=data,
            categoria=categoria,
            conta_id=conta_id,
            descricao=descricao
        )

        despesa_salva = DespesaRepository.criar_despesa(nova_despesa)
        ContaService.alterar_saldo(conta_id, valor)
        
        LogService.salvar_log(conta_id, f"Despesa na conta id: {conta_id} Criada")

        return despesa_salva.to_dict(), 201
    
    @staticmethod
    def get_despesas_por_conta(conta_id):
        despesas = DespesaRepository.get_despesas_por_conta(conta_id)

        if not despesas:
            return {"message": "Nenhuma despesa encontrada para esta conta"}, 404

        return [r.to_dict() for r in despesas], 200
    
    @staticmethod
    def get_por_id(despesa_id):
        despesa = DespesaRepository.get_por_id(despesa_id)

        if despesa is None:
            return {"mensagem": "Despesa não encontrada"}, 404

        return despesa.to_dict(), 200
    
    @staticmethod
    def editar_despesa(despesa_id, novo_valor, nova_data, nova_categoria, nova_descricao):
        despesa = Despesa.query.options(joinedload(Despesa.conta)).filter_by(id=despesa_id).first()
        
        if not despesa:
            return None, 404

        novo_valor = -abs(float(novo_valor))
        diferenca_valor = Decimal(novo_valor) - Decimal(str(despesa.valor))

        despesa_editada = DespesaRepository.editar_despesa(despesa_id, {
        "valor": novo_valor,
        "data": nova_data,
        "categoria": nova_categoria,
        "descricao": nova_descricao
        })
        
        conta_id = despesa.conta.id  
        ContaService.alterar_saldo(conta_id, diferenca_valor)
        
        LogService.salvar_log(conta_id, f"Despesa id: {despesa_id} editada")

        return despesa_editada.to_dict(), 200

    @staticmethod
    def excluir_despesa(despesa_id):
        result = DespesaRepository.excluir_despesa(despesa_id)

        if result is None:
            return {"error": "Despesa não encontrada"}, 404

        valor, conta_id = result
        ContaService.alterar_saldo(conta_id, -Decimal(valor))
        
        LogService.salvar_log(conta_id, f"Despesa id: {despesa_id} excluida")
        
        return {"message": "Despesa excluída com sucesso"}, 200