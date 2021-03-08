import json

from flask import request
from flask_restplus import Resource
from agro.utils.response import AgroResponse

from agro.blueprints.services.categoria import CategoriaService

class CategoriaResource(Resource):
    def get(self):
        agro_response = AgroResponse()
        categoria = CategoriaService()

        retorno = categoria.listar()
        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400("Não foi possível", "encontrar")
    
    def post(self):
        agro_response = AgroResponse()
        categoria = CategoriaService()
        dados = json.loads(request.data)

        retorno = categoria.criar(dados)
        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400("Falha na criação", "criação falhou")

    def delete(self, id):
        agro_response = AgroResponse()
        categoria = CategoriaService()

        retorno = categoria.deletar(id)
        if retorno:
            return agro_response.status_200(retorno)

    def put(self):
        agro_response = AgroResponse()
        categoria = CategoriaService()
        dados = json.loads(request.data)
        retorno = categoria.atualizar(dados)

        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400('deu', 'ruim')