from agro.models import Cliente
from agro.ext.database import db

class ClienteService():
    @staticmethod
    def criar(dados):
        cliente = Cliente(**dados)
        try:
            db.session.add(cliente)
            db.session.commit()
            return True
        finally:
            db.session.close()

    @staticmethod
    def listar():
        clientes = Cliente.query.all()
        return {"clientes": [cliente.to_dict(rules=('endereco_id', 'endereco.rua')) for cliente in clientes]}
