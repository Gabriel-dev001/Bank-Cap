from app import db

class Cripto(db.Model):
    __tablename__ = 'cripto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    conta_id = db.Column(db.Integer, db.ForeignKey('conta.id', ondelete='CASCADE'), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    valor_reais = db.Column(db.Numeric(10, 2), nullable=False)
    valor_cripto = db.Column(db.Numeric(30, 18), nullable=False)
    vendido = db.Column(db.Boolean, default=False, nullable=False)
    valor_cripto_vendido = db.Column(db.Numeric(30, 18), nullable=True)
    valor_reais_vendido = db.Column(db.Numeric(10, 2), nullable=True)
    criado_em = db.Column(db.Date, nullable=False) 
    conta = db.relationship('Conta', backref=db.backref('criptos', lazy=True, cascade='all, delete-orphan'))

    def __init__(self, conta_id, nome, valor_reais, valor_cripto, criado_em, vendido=False, valor_cripto_vendido=None, valor_reais_vendido=None):
        self.conta_id = conta_id
        self.nome = nome
        self.valor_reais = valor_reais
        self.valor_cripto = valor_cripto
        self.vendido = vendido
        self.valor_cripto_vendido = valor_cripto_vendido
        self.valor_reais_vendido = valor_reais_vendido
        self.criado_em = criado_em

    def to_dict(self):
        return {
            "id": self.id,
            "conta_id": self.conta_id,
            "nome": self.nome,
            "valor_reais": float(self.valor_reais),
            "valor_cripto": float(self.valor_cripto),
            "vendido": self.vendido,
            "valor_cripto_vendido": float(self.valor_cripto_vendido) if self.valor_cripto_vendido else None,
            "valor_reais_vendido": float(self.valor_reais_vendido) if self.valor_reais_vendido else None,
            "criado_em": self.criado_em.strftime("%Y-%m-%d %H:%M:%S") if self.criado_em else None
        }
