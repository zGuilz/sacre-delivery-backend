import json

from flask import request
from flask_restplus import Resource
from agro.utils.response import AgroResponse
from agro.ext.database import db
from agro.models import Usuario

from agro.utils.authenticate import jwt_required


class ConfirmacaoResource(Resource):
    def get(self, token):
        agro_response = AgroResponse()
        usuario = Usuario()
        resposta = None
        email = usuario.confirmacao_token(token)
        usuario = Usuario.query.filter_by(email=email).first()
        if not email:
            return agro_response.status_200('Link inválido ou expirado!')

        if usuario.confirmado:
            return agro_response.status_200('Conta já confirmada. Faça o login!')

        if usuario.email == email:
            usuario.confirmado = True
            db.session.add(usuario)
            db.session.commit()
            resposta = 'Você confirmou sua conta! Obrigado!'
        return agro_response.status_200(resposta)
