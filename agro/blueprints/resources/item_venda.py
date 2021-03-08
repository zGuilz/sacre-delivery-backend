import json

from flask import request
from flask_restplus import Resource
from agro.utils.response import AgroResponse

from agro.blueprints.services.item_venda import ItemVendaService

class ItemVendaResource(Resource):
    def get(self):
        agro_response = AgroResponse()
        item_venda = ItemVendaService()

        retorno = item_venda.listar()
        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400('deu', 'ruim')
    
    def post(self):
        agro_response = AgroResponse()
        item_venda = ItemVendaService()
        dados = json.loads(request.data)

        retorno = item_venda.criar(dados)
        if retorno:
            return agro_response.status_200('Item venda criado')
        return agro_response.status_400('deu', 'ruim')
    
    def delete(self, id):
        agro_response = AgroResponse()
        item_venda = ItemVendaService()

        retorno = item_venda.deletar(id)
        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400('deu', 'ruim')
    
    def put(self):
        agro_response = AgroResponse()
        item_venda = ItemVendaService()
        dados = json.loads(request.data)
        retorno = item_venda.atualizar(dados)
    
        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400('deu', 'ruim')
        