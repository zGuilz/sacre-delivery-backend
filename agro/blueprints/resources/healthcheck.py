from flask_restplus import Resource
from agro.utils.response import AgroResponse

class HealthCheckResource(Resource):
    def get(self):
        agro_response = AgroResponse()
        return agro_response.status_200('1.1.1')
