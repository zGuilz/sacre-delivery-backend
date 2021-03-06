import json

from flask import request
from flask_restplus import Resource
from agro.utils.response import AgroResponse

from agro.blueprints.services.cliente import ClienteService

class ClienteResource(Resource):
    def get(self):
        agro_response = AgroResponse()
        cliente = ClienteService()

        retorno = cliente.listar()
        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400('deu', 'ruim')

    def post(self):
        agro_response = AgroResponse()
        cliente = ClienteService()
        dados = json.loads(request.data)

        retorno = cliente.criar(dados)
        if retorno:
            return agro_response.status_200('Criado com sucesso')
        return agro_response.status_400('deu', 'ruim')
