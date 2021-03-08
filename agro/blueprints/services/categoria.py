from agro.models import Categoria
from agro.ext.database import db

class CategoriaService():
    @staticmethod
    def criar(dados):
        categoria = Categoria(**dados)
        db.session.add(categoria)
        db.session.commit()
        db.session.close()
        return True
    
    @staticmethod
    def listar():
        categorias = Categoria.query.all()
        return {"categorias": [categoria.to_dict(rules=('-categoria', '-categoria')) for categoria in categorias]}
    
    @staticmethod
    def deletar(id):
        categoria = Categoria.query.filter(Categoria.id == id).one()
        db.session.delete(categoria)
        db.session.commit()
        db.session.close()
        return True
    
    @staticmethod
    def atualizar(dados):
        categoria = Categoria.query.filter(Categoria.id == dados['id']).one()
        categoria.nome = dados['nome']
        categoria.descricao = dados['descricao']

        try:
            db.session.commit()
            return True
        finally:
            db.session.close()
