from agro.ext.database import db
from sqlalchemy_serializer import SerializerMixin

class Usuario(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(20), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'usuario',
        'polymorphic_on': type
    }

class Agricultor(Usuario, SerializerMixin):
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'agricultor'
    }

class Cliente(Usuario, SerializerMixin):
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    endereco_id = db.Column(db.Integer, db.ForeignKey("endereco.id"))
    serialize_rules = ('-endereco.endereco',)

    endereco = db.relationship("Endereco", backref="endereco")

    __mapper_args__ = {
        'polymorphic_identity': 'cliente'
    }

class Endereco(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(100), nullable=False)
    rua = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    casa = db.Column(db.String(100), nullable=False)

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
