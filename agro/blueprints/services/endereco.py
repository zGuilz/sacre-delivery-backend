from agro.models import Endereco
from agro.ext.database import db

class EnderecoService():
    @staticmethod
    def criar(dados):
        endereco = Endereco(**dados)
        try:
            db.session.add(endereco)
            db.session.commit()
            return True
        finally:
            db.session.close()
    
    @staticmethod
    def listar():
        enderecos = Endereco.query.all()
        return {"enderecos": [endereco.to_dict(rules=('-endereco', '-endereco')) for endereco in enderecos]}

    @staticmethod
    def deletar(id):
        endereco = Endereco.query.filter(Endereco.id == id).one()
        db.session.delete(endereco)
        db.session.commit()
        db.session.close()
        return True

    @staticmethod
    def atualizar(dados):
        endereco = Endereco.query.filter(Endereco.id == dados['id']).one()
        endereco.cep = dados['cep']
        endereco.rua = dados['rua']
        endereco.numero = dados['numero']
        endereco.casa = dados['casa']

        try:
            db.session.commit()
            return True
        finally:
            db.session.close()