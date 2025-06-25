from flask import request, jsonify, Response
import json
from app.service.receita_service import ReceitaService
from flask_jwt_extended import jwt_required

class ReceitaController:    
    @staticmethod
    @jwt_required()
    def criar_receita():
        print("Headers:", request.headers)
        print("JSON:", request.get_json())
        print("Data:", request.data)
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
    
    @staticmethod
    def get_receitas_por_conta(conta_id):
        receitas, status = ReceitaService.get_receitas_por_conta(conta_id)
        return Response(json.dumps(receitas, ensure_ascii=False),status=status,mimetype="application/json")
    
    @staticmethod
    def get_por_id(receita_id):
        receita, status = ReceitaService.get_por_id(receita_id)
        return Response(json.dumps(receita, ensure_ascii=False), status=status, mimetype="application/json")
    
    @staticmethod
    @jwt_required()
    def editar_receita(receita_id):
        data = request.get_json()
        if not all(k in data for k in ("valor", "data", "categoria")):
            return jsonify({"erro": "Dados incompletos"}), 400

        try:
            valor = data["valor"]
            data_receita = data["data"]
            categoria = data["categoria"]
            descricao = data.get("descricao")

            receita, status = ReceitaService.editar_receita(
                receita_id, valor, data_receita, categoria, descricao
            )

            if not receita:
                return jsonify({"erro": "Receita não encontrada"}), 404

            return Response(json.dumps(receita, ensure_ascii=False), status=status, mimetype="application/json")

        except Exception as e:
            return jsonify({"erro": str(e)}), 500

    
    @staticmethod
    @jwt_required()
    def excluir_receita(receita_id):
        response, status = ReceitaService.excluir_receita(receita_id)
        return jsonify(response), status