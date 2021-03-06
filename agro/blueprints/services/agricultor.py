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
    def listar():
        agricultores = Agricultor.query.all()
        return {"agricultores": [agricultor.to_dict(rules=('-agricultor', '-agricultor')) for agricultor in agricultores]}
