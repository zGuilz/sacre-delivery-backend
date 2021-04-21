import json

from flask import request
from flask_restplus import Resource
from agro.utils.response import AgroResponse
from agro.utils.authenticate import jwt_required

from agro.blueprints.services.endereco import EnderecoService


class EnderecoResource(Resource):
    def get(self):
        agro_response = AgroResponse()
        endereco = EnderecoService()

        retorno = endereco.listar()
        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400("Não foi possível", "encontrar")
    
    @jwt_required
    def post(self):
        agro_response = AgroResponse()
        endereco = EnderecoService()
        dados = json.loads(request.data)

        retorno = endereco.criar(dados)
        if retorno:
            return agro_response.status_200("Endereço criado")
        return agro_response.status_400("Falha na criação", "criação falhou")

    def delete(self, id):
        agro_response = AgroResponse()
        endereco = EnderecoService()

        retorno = endereco.deletar(id)
        if retorno:
            return agro_response.status_200(retorno)

    def put(self):
        agro_response = AgroResponse()
        endereco = EnderecoService()
        dados = json.loads(request.data)
        retorno = endereco.atualizar(dados)

        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400('deu', 'ruim')