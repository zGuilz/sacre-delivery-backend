from datetime import datetime

from flask import current_app

class AgroResponse():
    def __init__(self):
        status = 200
        mensagem = 'Operação realizada com sucesso'
        timestamp = str(datetime.now().isoformat())
        dados = {}
        sigla_projeto = current_app.config.get('APP_NAME')
        self.response = {
            "projeto": sigla_projeto,
            "dados": dados,
            "txMensagem": mensagem,
            "nrStatus": status,
            "timestamp": timestamp
        }
        super(AgroResponse, self).__init__()
    
    def status_200(self, dados):
        self.response['dados'] = dados
        return self.response, 200

    def status_201(self, dados):
        self.response['dados'] = dados
        return self.response, 201
    
    def status_400(self, mensagem, detalhe):
            del self.response['txMensagem']
            dados = {}
            dados['mensagem'] = mensagem
            dados['detalhe'] = detalhe

            self.response['dados'] = dados
            self.response['nrStatus'] = 400

            return self.response, 400

    def status_500(self, mensagem, detalhe, dados_tecnicos):
        del self.response['txMensagem']
        dados = {}
        dados['mensagem'] = mensagem
        dados['detalhe'] = f'{detalhe}\n{dados_tecnicos}'

        self.response['dados'] = dados
        self.response['nrStatus'] = 500

        return self.response, 500
