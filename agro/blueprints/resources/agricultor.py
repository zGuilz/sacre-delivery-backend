from flask import jsonify

from flask_restplus import Resource

from agro.blueprints.services.agricultor import AgricultorService

class AgricultorResource(Resource):
    def get(self):
        agricultor = AgricultorService()
        response = agricultor.testando()
        return jsonify(response)
