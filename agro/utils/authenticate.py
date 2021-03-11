from functools import wraps

import jwt
from flask import request, jsonify, current_app

from agro.models import Usuario

def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        
        if not token:
            return jsonify(error="Token não informado")

        if not 'Bearer' in token:
            return jsonify(error="Token inválido")

        try:
            token_puro = token.replace("Bearer ", "")
            decoded = jwt.decode(token_puro, current_app.config['SECRET_KEY'], algorithms="HS256")
            current_user = Usuario.query.get(decoded['id'])
        except:
            return jsonify(error="Token inválido")

        return f(current_user=current_user, *args, **kwargs)
    return wrapper
