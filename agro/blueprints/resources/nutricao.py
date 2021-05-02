import json

from flask import request
from flask_restplus import Resource
from agro.utils.response import AgroResponse

from agro.blueprints.services.nutricao import NutricaoService

class NutricaoResource(Resource):
    def get(self, alimento):
        agro_response = AgroResponse()
        nutricao = NutricaoService()

        retorno = nutricao.listar(alimento)
        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400('Não encontrado', 'False')
