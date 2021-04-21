from agro.models import Pedido
from agro.ext.database import db
from agro.utils.picpay import PicPay

class PedidoService():
    @staticmethod
    def criar(dados, current_user):
        picpay = PicPay()
        # payment = picpay.payment(
        #     reference_id=3,
        #     callback_url="https://picpay.com/site",
        #     return_url="http://www.sualoja.com.br/cliente/pedido/102030",
        #     value=1.0,
        #     expires_at="2022-05-01T16:00:00-03:00",
        #     buyer={
        #         "firstName": "João",
        #         "lastName": "Da Silva",
        #         "document": "123.456.789-10",
        #         "email": "teste@picpay.com",
        #         "phone": "+55 27 12345-6789",
        #     },
        # )
        print(current_user)
        pedido = Pedido(**dados)
        db.session.add(pedido)
        db.session.commit()
        db.session.close()
        return True
    
    @staticmethod
    def listar():
        pedidos = Pedido.query.all()
        return {"pedidos": [pedido.to_dict(rules=("-pedido", "-pedido")) for pedido in pedidos]}

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