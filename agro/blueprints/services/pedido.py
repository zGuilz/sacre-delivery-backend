from agro.models import Pedido
from agro.ext.database import db

class PedidoService():
    @staticmethod
    def criar(dados):
        pedido = Pedido(**dados)
        db.session.add(pedido)
        db.session.commit()
        db.session.close()
        return True
    
    @staticmethod
    def listar():
        pedidos = Pedido.query.all()
        return {"pedidos": [pedido.to_dict(rules=('-pedido', '-pedido')) for pedido in pedidos]}

    @staticmethod
    def deletar(id):
        pedido = Pedido.query.filter(Pedido.id == id).one()
        db.session.delete(pedido)
        db.session.commit()
        db.session.close()
        return True
    
    @staticmethod
    def atualizar(dados):
        pedido = Pedido.query.filter(Pedido.id == dados['id']).one()
        pedido.numero = dados['numero']
        pedido.preco_total = dados['preco_total']
        pedido.data = dados['data']
        pedido.forma_pagamento_id = dados['forma_pagamento_id']

        db.session.commit()
        db.session.close()
        return True