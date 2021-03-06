import json

from flask import request
from flask_restplus import Resource
from agro.utils.response import AgroResponse

from agro.blueprints.services.agricultor import AgricultorService

class AgricultorResource(Resource):
    def get(self):
        agro_response = AgroResponse()
        agricultor = AgricultorService()

        retorno = agricultor.listar()
        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400('deu', 'ruim')

    def post(self):
        agro_response = AgroResponse()
        agricultor = AgricultorService()
        dados = json.loads(request.data)

        retorno = agricultor.criar(dados)
        if retorno:
            return agro_response.status_200('criado fdp')
        return agro_response.status_400('deu', 'ruim')