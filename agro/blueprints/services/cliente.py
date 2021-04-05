from flask import url_for, render_template, request

from agro.models import Cliente
from agro.ext.database import db

from agro.utils.envio_email import enviar_email

class ClienteService():
    @staticmethod
    def criar(dados):
        cliente = Cliente(**dados)
        try:
            db.session.add(cliente)
            db.session.commit()

            token = cliente.gerar_token_confirmacao(cliente.email)
            confirmar_url = request.host_url + "api/confirmar/" + token
            html = render_template('confirmacao.html', confirmar_url=confirmar_url)
            descricao = 'Seja bem-vindo'
            enviar_email(cliente.email, descricao, html)
            return True
        finally:
            db.session.close()
    
    @staticmethod
    def atualizar(id, dados):
        cliente = Cliente.query.filter(Cliente.id == id).first()
        if cliente:
            for key, value in dados.items():
                if dados[key] is not None:
                    setattr(cliente, key, value)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def deletar(id):
        cliente = Cliente.query.filter(Cliente.id == id).one()
        try:
            db.session.delete(cliente)
            db.session.commit()
            db.session.close()
            return True
        except:
            return False

    @staticmethod
    def listar():
        clientes = Cliente.query.all()
        return {"clientes": [cliente.to_dict(rules=('endereco_id', 'endereco.rua', '-senha_hash')) for cliente in clientes]}
