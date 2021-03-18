import json

from flask import request
from flask_restplus import Resource
from agro.utils.response import AgroResponse
from agro.ext.database import db
from agro.models import Usuario


class ConfirmacaoResource(Resource):
    def get(self, token):
        agro_response = AgroResponse()
        usuario = Usuario()
        resposta = None
        try:
            email = usuario.confirmacao_token(token)
        except:
            resposta = 'Link inválido ou expirado'
        usuario = Usuario.query.filter_by(email=email)

        if usuario.confirmado:
            resposta = 'Conta confirmada. Faça o login'
        else:
            usuario.confirmado = True
            db.session.add(usuario)
            db.session.commit()
            resposta = 'Você confirmou sua conta! Obrigado!'
        return agro_response.status_200(resposta)
