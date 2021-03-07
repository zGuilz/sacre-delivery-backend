from agro.models import Produto
from agro.ext.database import db

class ProdutoService():
    @staticmethod
    def criar(dados):
        produto = Produto(**dados)
        db.session.add(produto)
        db.session.commit()
        db.session.close()
        return True
    
    @staticmethod
    def listar():
        produtos = Produto.query.all()
        return {"produtos": [produto.to_dict(rules=('-produto', '-produto')) for produto in produtos]}
    
    @staticmethod
    def deletar(id):
        produto = Produto.query.filter(Produto.id == id).one()
        db.session.delete(produto)
        db.session.commit()
        db.session.close()
        return True

    @staticmethod
    def atualizar(dados):
        produto = Produto.query.filter(Produto.id == dados['id']).one()
        produto.nome = dados["nome"]
        produto.preco = dados["preco"]
        produto.quantidade = dados['quantidade']
        produto.agricultor_id = dados["agricultor_id"]
        produto.categoria_id = dados["categoria_id"]
        db.session.commit()
        db.session.close()
        return True
