from flask import request, jsonify, Response
import json
from app.service.receita_service import ReceitaService
class ReceitaController:
    @staticmethod
    def criar_receita():
        data = request.get_json()

        campos_obrigatorios = ("conta_id", "valor", "data", "categoria", "descricao")
        if not all(campo in data for campo in campos_obrigatorios):
            return jsonify({"error": "Dados incompletos"}), 400

        conta_id = data["conta_id"]
        valor = data["valor"]
        data_receita = data["data"]
        categoria = data["categoria"]
        descricao = data.get("descricao")

        receita, status = ReceitaService.criar_receita(valor, data_receita, categoria, conta_id, descricao)
        return Response(json.dumps(receita, ensure_ascii=False), status=status, mimetype="application/json")
