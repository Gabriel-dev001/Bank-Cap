from app.models.log_model import Log
from extensions import db

class LogRepository:

    @staticmethod
    def salvar_log(origem_id, comentario):
        novo_log = Log(origem_id=origem_id, comentario=comentario)
        db.session.add(novo_log)
        db.session.commit()
        return novo_log
