from datetime import timedelta

from agro.models import Pedido
from agro.ext.database import db
from agro.utils.picpay import PicPay

class PedidoService():
    @staticmethod
    def criar(dados, current_user):
        picpay = PicPay()
        pedido = Pedido(**dados)
        db.session.add(pedido)
        db.session.flush()

        expiraca_em = (pedido.data.replace(microsecond=0) + timedelta(minutes=1)).isoformat() + "-03:00"

        payment = picpay.payment(
            reference_id=pedido.id,
            callback_url="https://picpay.com/site",
            return_url="http://www.sualoja.com.br/cliente/pedido/102030",
            value=dados["preco_total"],
            expires_at=expiraca_em,
            buyer={
                "firstName": current_user.nome,
                "lastName": current_user.sobrenome,
                "document": current_user.cpf,
                "email": current_user.email,
                "phone": current_user.telefone,
            },
        )
        db.session.commit()
        db.session.close()
        return payment
    
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