from flask import request, jsonify
from app.service.relatorio_service import RelatorioService

class RelatorioController:
    @staticmethod
    def gerar_relatorio(conta_id):
        data = request.get_json()
        relatorio = data.get("relatorio")
        data_inicial = data.get("data_inicial")
        data_final = data.get("data_final")

        if not relatorio:
            return jsonify({"error": "Informe o tipo do Relatório"}), 400

        resultado = RelatorioService.gerar_relatorio(relatorio, data_inicial, data_final, conta_id)
        return jsonify(resultado)