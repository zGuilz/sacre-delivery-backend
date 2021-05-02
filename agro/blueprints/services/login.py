from flask import current_app

import datetime
from agro.models import Usuario
import jwt


class LoginService():
    @staticmethod
    def logar(dados):
        usuario = Usuario.query.filter(Usuario.login == dados['login']).first()

        if not usuario.confirmado:
            return {'error': 'Usuário não confirmado'}

        if not usuario:
            return {'error': 'Usuário não encontrado'}

        if usuario.verifica_senha(dados['senha']):
            payload = {
                "id": usuario.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }
            token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm="HS256")
            return {
                "token": f'Bearer {token}'
            }
        return False
