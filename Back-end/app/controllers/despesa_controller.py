from flask import request, jsonify, Response
import json
from app.service.despesa_service import DespesaService

class DespesaController:
    @staticmethod
    def criar_despesa():
        data = request.get_json()

        campos_obrigatorios = ("conta_id", "valor", "data", "categoria", "descricao")
        if not all(campo in data for campo in campos_obrigatorios):
            return jsonify({"error": "Dados incompletos"}), 400

        conta_id = data["conta_id"]
        valor = data["valor"]
        data_despesa = data["data"]
        categoria = data["categoria"]
        descricao = data.get("descricao")

        despesa, status = DespesaService.criar_despesa(valor, data_despesa, categoria, conta_id, descricao)
        return Response(json.dumps(despesa, ensure_ascii=False), status=status, mimetype="application/json")
    
    @staticmethod
    def get_despesas_por_conta(conta_id):
        despessas, status = DespesaService.get_despesas_por_conta(conta_id)
        return Response(json.dumps(despessas, ensure_ascii=False),status=200,mimetype="application/json")
    
    @staticmethod
    def get_por_id(despesa_id):
        despesa, status = DespesaService.get_por_id(despesa_id)
        return Response(json.dumps(despesa, ensure_ascii=False), status=status, mimetype="application/json")
    
    @staticmethod
    def editar_despesa(despesa_id):
        data = request.get_json()
        if not all(k in data for k in ("valor", "data", "categoria")):
            return jsonify({"erro": "Dados incompletos"}), 400

        try:
            valor = data["valor"]
            data_despesa = data["data"]
            categoria = data["categoria"]
            descricao = data.get("descricao")

            despesa, status = DespesaService.editar_despesa(
                despesa_id, valor, data_despesa, categoria, descricao
            )

            if not despesa:
                return jsonify({"erro": "Despesa não encontrada"}), 404

            return Response(json.dumps(despesa, ensure_ascii=False), status=status, mimetype="application/json")

        except Exception as e:
            return jsonify({"erro": str(e)}), 500

    
    @staticmethod
    def excluir_despesa(despesa_id):
        response, status = DespesaService.excluir_despesa(despesa_id)
        return jsonify(response), status