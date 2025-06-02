from app.models.cripto_model import Cripto
from app.repository.cripto_repository import CriptoRepository
from app.service.conta_service import ContaService
from decimal import Decimal
import requests

from app.service.log_service import LogService

class CriptoService:
    @staticmethod
    def criar_cripto(data):
        conta_id = data.get("conta_id")
        nome = data.get("nome")
        data_str = data.get("data")
        valor_reais = Decimal(str(data.get("valor")))

        # 1. Verifica saldo
        saldo = ContaService.obter_saldo(conta_id)
        if valor_reais > saldo:
            raise ValueError("Saldo insuficiente.")

        # 2. Chamada à API Middleware Binance
        response = requests.put(
            "http://127.0.0.1:9000/api/historical-price/",
            json={"symbol": nome, "date": data_str}
        )

        if response.status_code != 200:
            raise Exception("Erro ao consultar a API da Binance.")

        preco_unitario = Decimal(response.json().get("price"))
        if preco_unitario <= 0:
            raise ValueError("Preço da cripto inválido.")

        # 3. Calcula valor em cripto
        valor_cripto = valor_reais / preco_unitario

        # 4. Cria e salva no banco
        nova_cripto = Cripto(
            conta_id=conta_id,
            nome=nome,
            valor_reais=valor_reais,
            valor_cripto=valor_cripto
        )
        
        LogService.salvar_log(conta_id, f"Cripto Adicionada na conta id: {conta_id}")

        return CriptoRepository.salvar(nova_cripto)

    @staticmethod
    def get_criptos_por_conta(conta_id):
        criptos = CriptoRepository.get_criptos_por_conta(conta_id)

        if not criptos:
            return {"message": "Nenhuma cripto encontrada para esta conta"}, 404

        return [c.to_dict() for c in criptos], 200

    @staticmethod
    def excluir_cripto(cripto_id):
        result = CriptoRepository.excluir_cripto(cripto_id)

        if result is None:
            return {"error": "Cripto não encontrada"}, 404

        valor_reais, conta_id = result
        ContaService.alterar_saldo(conta_id, float(valor_reais))
        
        LogService.salvar_log(conta_id, f"Cripto id: {cripto_id} excluida")

        return {"message": "Cripto excluída com sucesso"}, 200
