from flask import Blueprint, jsonify, request
from app.service.conta_service import ContaService


class ContaController:
    @staticmethod
    def criar_conta():
        data = request.get_json()
        
        if not all(key in data for key in ("usuario_id", "nome", "banco", "tipo")):
            return jsonify({"error": "Dados incompletos"}), 400
        
        return ContaService.criar_conta(
            data["usuario_id"], 
            data["nome"], 
            data["banco"], 
            data["tipo"], 
        )
    
    @staticmethod
    def listar_contas():
        contas = ContaService.listar_todos()
        return jsonify(contas), 200
