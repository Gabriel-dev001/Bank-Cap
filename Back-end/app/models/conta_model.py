from app import db

class Conta(db.Model):
    __tablename__ = 'conta'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete='CASCADE'), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    banco = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.Enum('PESSOAL', 'EMPRESARIAL', name='tipo_conta'), nullable=False)
    saldo = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)  # Novo atributo saldo
    criado_em = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    usuario = db.relationship('Usuario', backref=db.backref('contas', lazy=True, cascade='all, delete-orphan'))

    def __init__(self, usuario_id, nome, banco, tipo, saldo=0.00):
        self.usuario_id = usuario_id
        self.nome = nome
        self.banco = banco
        self.tipo = tipo
        self.saldo = saldo  # Adicionando saldo no construtor

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "nome": self.nome,
            "banco": self.banco,
            "tipo": self.tipo,
            "saldo": float(self.saldo),  # Convertendo Decimal para float
            "criado_em": self.criado_em.strftime("%Y-%m-%d %H:%M:%S") if self.criado_em else None
        }
