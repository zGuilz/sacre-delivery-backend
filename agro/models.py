from flask import current_app

from datetime import datetime
from agro.ext.database import db
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from itsdangerous import URLSafeTimedSerializer

class Usuario(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(20), nullable=False, unique=True)
    senha_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    confirmado = db.Column(db.Boolean(), default=False, nullable=False)
    criado_em = db.Column(db.DateTime(), default=datetime.now)
    type = db.Column(db.String(50))
    endereco_id = db.Column(db.Integer, db.ForeignKey("endereco.id"))
    serialize_rules = ('-endereco.endereco',)

    endereco = db.relationship("Endereco", backref="endereco")

    __mapper_args__ = {
        'polymorphic_identity': 'usuario',
        'polymorphic_on': type
    }

    @property
    def senha(self):
        raise AttributeError('senha não é atributo legível')

    @senha.setter
    def senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verifica_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    @staticmethod
    def gerar_token_confirmacao(email):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps(email, salt=current_app.config['SECURITY_PASSWORD_SALT'])
    
    @staticmethod
    def confirmacao_token(token, expiration=60):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            email = serializer.loads(
                token,
                salt=current_app.config['SECURITY_PASSWORD_SALT'],
                max_age=expiration
            )
        except Exception:
            return False
        return email

class Agricultor(Usuario, SerializerMixin):
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'agricultor'
    }

class Cliente(Usuario, SerializerMixin):
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'cliente'
    }

class Endereco(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(100), nullable=False)
    rua = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String(100), nullable=True)

class Produto(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categoria.id"), nullable=False)
    agricultor_id = db.Column(db.Integer, db.ForeignKey("agricultor.id"), nullable=False)
    serialize_rules = ('-categoria.categoria', '-agricultor.agricultor')

    categoria = db.relationship("Categoria", backref="categoria")
    agricultor = db.relationship("Agricultor", backref="agricultor")

class Categoria(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)

class FormaPagamento(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)

class Pedido(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    preco_total = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, default=datetime.now)
    forma_pagamento_id = db.Column(db.Integer, db.ForeignKey("forma_pagamento.id"), nullable=False)
    serialize_rules = ('-formapagamento.formapagamento',)

    forma_pagamento = db.relationship("FormaPagamento", backref="formapagamento")

class ItemVenda(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_por_item = db.Column(db.Float, nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey("produto.id"), nullable=False)
    pedido_id = db.Column(db.Integer, db.ForeignKey("pedido.id"), nullable=False)

    produto = db.relationship("Produto", backref="produto")
    pedido = db.relationship("Pedido", backref="pedido")