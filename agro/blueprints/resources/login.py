import json

from flask import request
from flask_restplus import Resource
from agro.utils.response import AgroResponse

from agro.blueprints.services.login import LoginService


class LoginResource(Resource):
    def post(self):
        agro_response = AgroResponse()
        login = LoginService()
        dados = json.loads(request.data)

        retorno = login.logar(dados)
        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_200(retorno)
