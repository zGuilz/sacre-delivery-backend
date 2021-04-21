import json

from flask import request
from flask_restplus import Resource
from agro.utils.response import AgroResponse
from agro.utils.authenticate import jwt_required

from agro.blueprints.services.pedido import PedidoService

class PedidoResource(Resource):
    def get(self):
        agro_response = AgroResponse()
        pedido = PedidoService()

        retorno = pedido.listar()
        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400("Não, encontrado")

    @jwt_required
    def post(self, current_user):
        agro_response = AgroResponse()
        pedido = PedidoService()
        dados = json.loads(request.data)

        retorno = pedido.criar(dados, current_user)
        if retorno:
            return agro_response.status_200("Pedido criado com sucesso!")
        return agro_response.status_400("Não, criado")

    def delete(self, id):
        agro_response = AgroResponse()
        pedido = PedidoService()

        retorno = pedido.deletar(id)
        if retorno:
            return agro_response.status_200("Pedido deletado com sucesso")
    
    def put(self):
        agro_response = AgroResponse()
        pedido = PedidoService()
        dados = json.loads(request.data)
        retorno = pedido.atualizar(dados)

        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400('deu', 'ruim')