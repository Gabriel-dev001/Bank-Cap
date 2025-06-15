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
        criado_em = data.get("data")

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

        # 2.1 Verifica se a resposta contém o preço 
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
            valor_cripto=valor_cripto,
            criado_em=criado_em
        )
        
        # 5. Atualiza o saldo da conta
        valor = -abs(float(valor_reais))
        ContaService.alterar_saldo(conta_id, float(valor))

        LogService.salvar_log(conta_id, f"Cripto Adicionada na conta id: {conta_id}")

        return CriptoRepository.salvar(nova_cripto)

    # @staticmethod
    # def criar_cripto(data):
    #     try:
    #         conta_id = data.get("conta_id")
    #         nome = data.get("nome")
    #         data_str = data.get("data")
    #         valor_reais = Decimal(str(data.get("valor")))

    #         # 1. Verifica saldo
    #         saldo = ContaService.obter_saldo(conta_id)
    #         print(f"Saldo da conta: {saldo}, Valor solicitado: {valor_reais}")
    #         if valor_reais > saldo:
    #             raise ValueError("Saldo insuficiente.")

    #         # 2. Chamada à API Middleware Binance
    #         response = requests.put(
    #             "http://127.0.0.1:9000/api/historical-price/",
    #             json={"symbol": nome, "date": data_str}
    #         )

    #         print(f"Status code da resposta: {response.status_code}")
    #         if response.status_code != 200:
    #             raise Exception("Erro ao consultar a API da Binance.")

    #         # 2.1 Verifica se a resposta contém o preço 
    #         response_json = response.json()
    #         print(f"Resposta da API: {response_json}")
    #         preco_unitario = response_json.get("price")
    #         print(f"Preço retornado pela API: {preco_unitario}")

    #         if preco_unitario is None:
    #             raise ValueError("Preço da cripto não retornado pela API.")
    #         preco_unitario = Decimal(preco_unitario)
    #         if preco_unitario <= 0:
    #             raise ValueError("Preço da cripto inválido.")

    #         # 3. Calcula valor em cripto
    #         valor_cripto = valor_reais / preco_unitario
    #         print(f"Valor em cripto calculado: {valor_cripto}")

    #         # 4. Cria e salva no banco
    #         nova_cripto = Cripto(
    #             conta_id=conta_id,
    #             nome=nome,
    #             valor_reais=valor_reais,
    #             valor_cripto=valor_cripto
    #         )
            
    #         LogService.salvar_log(conta_id, f"Cripto Adicionada na conta id: {conta_id}")

    #         return CriptoRepository.salvar(nova_cripto)
    #     except Exception as e:
    #         print(f"Erro ao criar cripto: {e}")
    #         return {"error": str(e)}, 500  
        
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
