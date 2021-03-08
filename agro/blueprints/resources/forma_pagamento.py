import json

from flask import request
from flask_restplus import Resource
from agro.utils.response import AgroResponse

from agro.blueprints.services.forma_pagamento import FormaPagamentoService

class FormaPagamentoResource(Resource):
    def get(self):
        agro_response = AgroResponse()
        forma_pagamento = FormaPagamentoService()

        retorno = forma_pagamento.listar()
        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400('Não foi possivel', 'pegar')
    
    def post(self):
        agro_response = AgroResponse()
        forma_pagamento = FormaPagamentoService()
        dados = json.loads(request.data)

        retorno = forma_pagamento.criar(dados)
        if retorno:
            return agro_response.status_200('Forma de pagamento criada!')
        return agro_response.status_400('Não foi possível', 'criar')
    
    def delete(self, id):
        agro_response = AgroResponse()
        forma_pagamento = FormaPagamentoService()

        retorno = forma_pagamento.deletar(id)
        if retorno:
            return agro_response.status_200("Forma de Pagamento deletada com sucesso!")

    def put(self):
        agro_response = AgroResponse()
        forma_pagamento = FormaPagamentoService()
        dados = json.loads(request.data)
        retorno = forma_pagamento.atualizar(dados)

        if retorno:
            return agro_response.status_200(retorno)
        return agro_response.status_400('deu', 'ruim')
            