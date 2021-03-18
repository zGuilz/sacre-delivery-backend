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
    
    def put(self, id):
        agro_response = AgroResponse()
        agricultor = AgricultorService()
        dados = json.loads(request.data)

        retorno = agricultor.atualizar(id, dados)
        if retorno:
            return agro_response.status_200(retorno)
    
    def delete(self, id):
        agro_response = AgroResponse()
        agricultor = AgricultorService()

        retorno = agricultor.deletar(id)
        if retorno:
            return agro_response.status_200(retorno)

    def post(self):
        agro_response = AgroResponse()
        agricultor = AgricultorService()
        dados = json.loads(request.data)

        retorno = agricultor.criar(dados)
        if retorno:
            return agro_response.status_200('Um e-mail de confirmação foi enviado pra você')
        return agro_response.status_400('deu', 'ruim')
