import json

from flask import request
from flask_restplus import Resource
from agro.utils.response import AgroResponse

from agro.blueprints.services.produto import ProdutoService

class ProdutoResource(Resource):
    def get(self):
        agro_response = AgroResponse()
        produto = ProdutoService()

        retorno = produto.listar()
        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400('deu', 'ruim')

    def post(self):
        agro_response = AgroResponse()
        produto = ProdutoService()
        dados = json.loads(request.data)

        retorno = produto.criar(dados)
        if retorno:
            return agro_response.status_200('Produto criado com sucesso')
        return agro_response.status_400('deu', 'ruim')

    def delete(self, id):
        agro_response = AgroResponse()
        produto = ProdutoService()

        retorno = produto.deletar(id)
        if retorno:
            return agro_response.status_200("Produto deletado com sucesso")

    def put(self):
        agro_response = AgroResponse()
        produto = ProdutoService()
        dados = json.loads(request.data)
        retorno =  produto.atualizar(dados)

        if retorno:
            return agro_response.status_200("Produto atualizado com sucesso")

