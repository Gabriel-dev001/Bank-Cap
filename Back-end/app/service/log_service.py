from app.repository.log_repository import LogRepository

class LogService:

    @staticmethod
    def salvar_log(origem_id, comentario):
        return LogRepository.salvar_log(origem_id, comentario)
