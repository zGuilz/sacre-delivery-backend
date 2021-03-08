from agro.models import FormaPagamento
from agro.ext.database import db

class FormaPagamentoService():
    @staticmethod
    def criar(dados):
        forma_pagamento = FormaPagamento(**dados)
        db.session.add(forma_pagamento)
        db.session.commit()
        db.session.close()
        return True

    @staticmethod 
    def listar():
        formas_pagamento = FormaPagamento.query.all()
        return {"formas_pagamento": [forma_pagamento.to_dict(rules=('-formapagamento', '-formapagamento')) for forma_pagamento in formas_pagamento]}

    @staticmethod
    def deletar(id):
        forma_pagamento = FormaPagamento.query.filter(FormaPagamento.id == id).one()
        db.session.delete(forma_pagamento)
        db.session.commit()
        db.session.close()
        return True

    @staticmethod
    def atualizar(dados):
        forma_pagamento = FormaPagamento.query.filter(FormaPagamento.id == dados['id']).one()
        forma_pagamento.tipo = dados['tipo']

        db.session.commit()
        db.session.close()
        return True
