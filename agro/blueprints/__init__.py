from flask import Blueprint
from flask_restplus import Api

from agro.blueprints.resources.agricultor import AgricultorResource

bp = Blueprint("restapi", __name__, url_prefix="/api")
api = Api(bp)

def init_app(app):
    api.add_resource(AgricultorResource, "/agricultor", methods=['GET'])
    app.register_blueprint(bp)