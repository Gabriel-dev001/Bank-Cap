from app import db

class Receita(db.Model):
    __tablename__ = 'receita'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    conta_id = db.Column(db.Integer, db.ForeignKey('conta.id', ondelete='CASCADE'), nullable=False)
    valor = db.Column(db.Numeric(10,2), nullable=False)
    data = db.Column(db.Date, nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(1000), nullable=True)
    criado_em = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    conta = db.relationship('Conta', backref=db.backref('receitas', lazy=True, cascade='all, delete-orphan'))

    def __init__(self, valor, data, categoria, conta_id, descricao=None):
        self.conta_id = conta_id
        self.valor = valor
        self.data = data
        self.categoria = categoria
        self.descricao = descricao

    def to_dict(self):
        return {
            "id": self.id,
            "conta_id": self.conta_id,
            "valor": float(self.valor),  # Converte Decimal para float
            "data": self.data.strftime("%Y-%m-%d") if self.data else None,  # Formata data
            "categoria": self.categoria,
            "descricao": self.descricao,
            "criado_em": self.criado_em.strftime("%Y-%m-%d %H:%M:%S") if self.criado_em else None
        }
