from flask import Blueprint, jsonify, request, Response
import json
from app.service.conta_service import ContaService


class ContaController:
    @staticmethod
    def criar_conta():
        data = request.get_json()
        
        if not all(key in data for key in ("usuario_id", "nome", "banco", "tipo")):
            return jsonify({"error": "Dados incompletos"}), 400
        
        response =  ContaService.criar_conta(
            data["usuario_id"], 
            data["nome"], 
            data["banco"], 
            data["tipo"], 
        )

        return Response(json.dumps(response, ensure_ascii=False), 
                    status=201, mimetype="application/json")
    
    
    @staticmethod
    def listar_contas():
        contas = ContaService.listar_todos()
        return Response(json.dumps(contas, ensure_ascii=False), 
                    status=200, mimetype="application/json")
