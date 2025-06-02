from app import db

class Log(db.Model):
    __tablename__ = 'log'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    origem_id = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.Text, nullable=True)
    criado_em = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, origem_id, comentario):
        self.origem_id = origem_id
        self.comentario = comentario

    def to_dict(self):
        return {
            "id": self.id,
            "origem_id": self.origem_id,
            "comentario": self.comentario,
            "criado_em": self.criado_em.strftime("%Y-%m-%d %H:%M:%S") if self.criado_em else None
        }
