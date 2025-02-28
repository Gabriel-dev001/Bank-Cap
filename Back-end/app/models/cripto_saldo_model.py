from app import db

class CriptoSaldo(db.Model):
    __tablename__ = 'cripto_saldo'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    conta_id = db.Column(db.Integer, db.ForeignKey('conta.id', ondelete='CASCADE'), nullable=False)
    nome_cripto = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Numeric(18,8), nullable=False)
    criado_em = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    conta = db.relationship('Conta', backref=db.backref('cripto_saldos', lazy=True, cascade='all, delete-orphan'))

    def __init__(self, nome_cripto, quantidade, conta_id):
        self.conta_id = conta_id
        self.nome_cripto = nome_cripto
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "id": self.id,
            "conta_id": self.conta_id,
            "nome_cripto": self.nome_cripto,
            "quantidade": float(self.quantidade),  # Converte Decimal para float
            "criado_em": self.criado_em.strftime("%Y-%m-%d %H:%M:%S") if self.criado_em else None  # Formata datetime
        }
