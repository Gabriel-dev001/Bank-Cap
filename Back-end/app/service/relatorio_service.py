from app.repository.relatorio_repository import RelatorioRepository
from datetime import datetime

class RelatorioService:
    @staticmethod
    def gerar_relatorio(relatorio, data_inicial, data_final, conta_id):
        if not data_inicial:
            data_inicial = "2000-01-01"
        if not data_final:
            data_final = datetime.today().strftime("%Y-%m-%d")


        if relatorio == 1:
            return RelatorioRepository.extrato_conta(data_inicial, data_final, conta_id)    
        elif relatorio == 2:
            return RelatorioRepository.relatorio_gastos(data_inicial, data_final, conta_id)
        elif relatorio == 3:
            return RelatorioRepository.relatorio_ganhos(data_inicial, data_final, conta_id)
        elif relatorio == 4:
            return RelatorioRepository.extrato_geral(data_inicial, data_final, conta_id)
        elif relatorio == 5:
            return RelatorioRepository.relatorio_transacoes_cripto(data_inicial, data_final, conta_id)
        else:
            return {"error": "Relatório não encontrado"}