from agro.models import ItemVenda
from agro.ext.database import db

class ItemVendaService():
    @staticmethod
    def criar(dados):
        item_venda = ItemVenda(**dados)
        db.session.add(item_venda)
        db.session.commit()
        db.session.close()
        return True
    
    @staticmethod
    def listar():
        itens_vendas = ItemVenda.query.all()
        return {"itens_vendas": [item_venda.to_dict(rules=('-item_venda', '-item_venda'))for item_venda in itens_vendas]}

    @staticmethod
    def deletar(id):
        item_venda = ItemVenda.query.filter(ItemVenda.id == id).one()
        db.session.delete(item_venda)
        db.session.commit()
        db.session.close()
        return True
    
    @staticmethod
    def atualizar(dados):
        item_venda = ItemVenda.query.filter(ItemVenda.id == dados['id']).one()
        item_venda.quantidade = dados['quantidade']
        item_venda.preco_por_item = dados['preco_por_item']
        item_venda.produto_id = dados['produto_id']
        item_venda.pedido_id = dados['pedido_id']

        try:
            db.session.commit()
            return True
        finally:
            db.session.close()