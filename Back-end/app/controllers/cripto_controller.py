from flask import request, jsonify, Response
import json
from app.service.cripto_service import CriptoService

class CriptoController:
    @staticmethod
    def criar_cripto():
        try:
            data = request.json
            cripto = CriptoService.criar_cripto(data)
            return jsonify(cripto.to_dict()), 201
        except ValueError as ve:
            return jsonify({"erro": str(ve)}), 400
        except Exception as e:
            return jsonify({"erro": "Erro interno", "detalhes": str(e)}), 500
        
    @staticmethod
    def vender_cripto(cripto_id):
        try:
            cripto = CriptoService.vender_cripto(cripto_id)
            return jsonify(cripto.to_dict()), 200
        except ValueError as ve:
            return jsonify({"erro": str(ve)}), 400
        except Exception as e:
            return jsonify({"erro": "Erro interno", "detalhes": str(e)}), 500
    
    @staticmethod
    def get_criptos_por_conta(conta_id):
        criptos, status = CriptoService.get_criptos_por_conta(conta_id)
        return Response(json.dumps(criptos, ensure_ascii=False), status=status, mimetype="application/json")
    
    @staticmethod
    def excluir_cripto(cripto_id):
        response, status = CriptoService.excluir_cripto(cripto_id)
        return jsonify(response), status
