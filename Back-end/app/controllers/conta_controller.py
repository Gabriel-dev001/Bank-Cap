from flask import Blueprint, jsonify, request, Response
import json
from app.service.conta_service import ContaService

from flask_jwt_extended import jwt_required

class ContaController:
    @staticmethod
    @jwt_required()
    def criar_conta():
        data = request.get_json()
        
        if not all(key in data for key in ("usuario_id", "nome", "banco", "tipo")):
            return jsonify({"error": "Dados incompletos"}), 400
        
        response, status = ContaService.criar_conta(
            data["usuario_id"], 
            data["nome"], 
            data["banco"], 
            data["tipo"]
        )

        return Response(json.dumps(response, ensure_ascii=False), 
                    status=201, mimetype="application/json")
    
    @staticmethod
    def get_contas():
        contas = ContaService.get_contas()
        return Response(json.dumps(contas, ensure_ascii=False), 
                    status=200, mimetype="application/json")

    @staticmethod
    def get_by_id_contas(conta_id):
        conta = ContaService.get_by_id_conta(conta_id)

        if conta:
            return Response(json.dumps(conta.to_dict(), ensure_ascii=False), status=200, mimetype="application/json")
            
        return Response(json.dumps({"erro": "Conta não encontrado"}), status=404, mimetype="application/json")

    @staticmethod
    @jwt_required()
    def editar_conta(conta_id):
        data = request.get_json()
        response, status_code = ContaService.editar_conta(conta_id, data)

        return Response(json.dumps(response, ensure_ascii=False), 
                        status=status_code, mimetype="application/json")
        
    @staticmethod
    def get_contas_usuario(usuario_id):
        contas, status = ContaService.get_contas_usuario(usuario_id)
        return Response(json.dumps(contas, ensure_ascii=False), status=status, mimetype='application/json')

    @staticmethod
    @jwt_required()
    def deletar_conta(conta_id):
        response, status_code = ContaService.deletar_conta(conta_id)

        return Response(json.dumps(response, ensure_ascii=False), 
                        status=status_code, mimetype="application/json")  
    
    @staticmethod
    def alterar_saldo():
        data = request.get_json()

        if not all(key in data for key in ("conta_id", "valor")):
            return False

        try:
            conta_id = data["conta_id"]
            valor = float(data["valor"])

            sucesso = ContaService.alterar_saldo(conta_id, valor)
            return sucesso
        except Exception as e:
            print(f"Erro ao alterar saldo: {e}") 
            return False