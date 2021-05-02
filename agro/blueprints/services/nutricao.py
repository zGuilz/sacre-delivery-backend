from agro.utils.edamam import Edamam

class NutricaoService():

    def __init__(self):
        self.edamam_api = Edamam()

    def listar(self, alimento):
        alimento = self.edamam_api.get_food(alimento)

        return alimento
