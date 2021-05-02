import json

from flask import request
from flask_restplus import Resource
from agro.utils.response import AgroResponse
from agro.utils.authenticate import jwt_required

from agro.blueprints.services.cliente import ClienteService


class ClienteResource(Resource):
    def get(self):
        agro_response = AgroResponse()
        cliente = ClienteService()

        retorno = cliente.listar()
        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400('deu', 'ruim')
    
    @jwt_required
    def put(self, current_user):
        agro_response = AgroResponse()
        cliente = ClienteService()
        dados = json.loads(request.data)

        retorno = cliente.atualizar(current_user.id, dados)
        if retorno:
            return agro_response.status_200(retorno)
    
    def delete(self, id):
        agro_response = AgroResponse()
        cliente = ClienteService()

        retorno = cliente.deletar(id)
        if retorno:
            return agro_response.status_200(retorno)

    def post(self):
        agro_response = AgroResponse()
        cliente = ClienteService()
        dados = json.loads(request.data)

        retorno = cliente.criar(dados)
        if retorno:
            return agro_response.status_200('Um e-mail de confirmação foi enviado pra você')
        return agro_response.status_400('deu', 'ruim')
