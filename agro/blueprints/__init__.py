import sys
import traceback
from werkzeug.exceptions import NotFound

from flask_restplus import Api

from agro.blueprints.resources.healthcheck import HealthCheckResource
from agro.blueprints.resources.agricultor import AgricultorResource
from agro.blueprints.resources.cliente import ClienteResource
from agro.blueprints.resources.pedido import PedidoResource
from agro.blueprints.resources.forma_pagamento import FormaPagamentoResource
from agro.blueprints.resources.endereco import EnderecoResource
from agro.blueprints.resources.item_venda import ItemVendaResource
from agro.blueprints.resources.categoria import CategoriaResource
from agro.blueprints.resources.produto import ProdutoResource
from agro.utils.response import AgroResponse

BASE_PATH = '/api'

def init_app(app):
    api = Api(
        doc='/v1/api-docs',
        version='0.0.1',
        base_url=BASE_PATH,
        default_mediatype='application/json',
        catch_all_404s=True,
        path=BASE_PATH
    )

    api.add_resource(HealthCheckResource, f'{BASE_PATH}/health', methods=['GET'])
    api.add_resource(AgricultorResource, f'{BASE_PATH}/agricultor', methods=['GET', 'POST'])
    api.add_resource(ClienteResource, f'{BASE_PATH}/cliente', methods=['GET', 'POST'])
    api.add_resource(PedidoResource, f'{BASE_PATH}/pedido', methods=['GET', 'POST', 'PUT'])
    api.add_resource(PedidoResource, f'{BASE_PATH}/pedido/<string:id>', methods=['DELETE'])
    api.add_resource(FormaPagamentoResource, f'{BASE_PATH}/forma-pagamento', methods=['GET', 'POST', 'PUT'])
    api.add_resource(FormaPagamentoResource, f'{BASE_PATH}/forma-pagamento/<string:id>', methods=['DELETE'])
    api.add_resource(EnderecoResource, f'{BASE_PATH}/endereco', methods=['GET', 'POST', 'PUT'])
    api.add_resource(EnderecoResource, f'{BASE_PATH}/endereco/<string:id>', methods=['DELETE'])
    api.add_resource(ItemVendaResource, f'{BASE_PATH}/item-venda', methods=['GET', 'POST', 'PUT'])
    api.add_resource(ItemVendaResource, f'{BASE_PATH}/item-venda/<string:id>', methods=['DELETE'])
    api.add_resource(CategoriaResource, f'{BASE_PATH}/categoria', methods=['GET', 'POST', 'PUT'])
    api.add_resource(CategoriaResource, f'{BASE_PATH}/categoria/<string:id>', methods=['DELETE'])
    api.add_resource(ProdutoResource, f'{BASE_PATH}/produto', methods=['GET', 'POST', 'PUT'])
    api.add_resource(ProdutoResource, f'{BASE_PATH}/produto/<string:id>', methods=['DELETE'])

    @api.errorhandler(NotFound)
    def page_not_found_error(error):
        ultron_response = AgroResponse()
        mensagem = 'Erro de parâmetro(s) inválido(s).'
        detalhe = [str(error)]
        return ultron_response.status_400(mensagem, detalhe)
    
    @api.errorhandler(Exception)
    def default_error_handler(e: Exception):
        agro_response = AgroResponse()
        exc_type, exc_value, exc_traceback = sys.exc_info()
        mensagem = 'Erro interno'
        dados_tecnicos = {
            'arquivo': exc_traceback.tb_frame.f_code.co_filename,
            'linha': exc_traceback.tb_lineno,
            'nome': exc_traceback.tb_frame.f_code.co_name,
            'tipo': get_type_or_class_name(exc_type),
            'mensagem': str(exc_value),
            'traceback': traceback.format_exc()
        }
        detalhe = str(exc_value)
        return agro_response.status_500(mensagem, detalhe, dados_tecnicos)
    
    def get_type_or_class_name(var):
        if type(var).__name__ == 'type':
            return var.__name__
        else:
            return type(var).__name__

    api.init_app(app)
