from agro.models import Agricultor
from agro.ext.database import db

class AgricultorService():
    @staticmethod
    def criar(dados):
        agricultor = Agricultor(**dados)
        db.session.add(agricultor)
        db.session.commit()
        db.session.close()
        return True
    
    @staticmethod
    def atualizar(id, dados):
        agricultor = Agricultor.query.filter(Agricultor.id == id).first()
        if agricultor:
            for key, value in dados.items():
                if dados[key] is not None:
                    setattr(agricultor, key, value)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def deletar(id):
        agricultor = Agricultor.query.filter(Agricultor.id == id).one()
        try:
            db.session.delete(agricultor)
            db.session.commit()
            db.session.close()
            return True
        except:
            return False

    @staticmethod
    def listar():
        agricultores = Agricultor.query.all()
        return {"agricultores": [agricultor.to_dict(rules=('-agricultor', '-senha_hash')) for agricultor in agricultores]}
