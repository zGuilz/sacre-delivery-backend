import os
import requests
from dotenv import load_dotenv
from deep_translator import GoogleTranslator

load_dotenv()

NTR_code = {
    "CA": "Calcium",
    "ENERC_KCAL": "Energy",
    "CHOCDF": "Carboidrato",
    "NIA":	"Niacin",
    "CHOLE": "Cholesterol",
    "P": "Phosphorus",
    "FAMS":	"Monounsaturated",
    "PROCNT": "Protein",
    "FAPU":	"Polyunsaturated",
    "RIBF":	"Riboflavin",
    "FASAT": "Saturated",
    "SUGAR": "Sugars",
    "FAT":	"Gordura",
    "THIA":	"Thiamin",
    "FATRN": "Trans",
    "TOCPHA": "Vitamin E",
    "FE": "Iron",
    "VITA_RAE":	"Vitamin A",
    "FIBTG": "Fiber",
    "VITB12": "Vitamin B12",
    "FOLDFE": "Folate",
    "VITB6A": "Vitamin B6",
    "K": "Potassium",
    "VITC":	"Vitamin C",
    "MG": "Magnesium",
    "VITD": "Vitamin D",
    "NA": "Sodium",
    "VITK1": "Vitamin K"
}


class Edamam:

    __URL = "https://api.edamam.com/api/food-database/v2/"

    def __init__(self):
        self.application_id = os.environ.get('APP_ID')
        self.api_key = os.environ.get('API_KEY_EDAMAM')
    
    def __get_url(self, req='parser'):
        return f"{self.__URL}/{req}?app_id={self.application_id}&app_key={self.api_key}"

    def __translate_message(self, message, target="en"):
        self.translator = GoogleTranslator(source='auto', target=target)
        message_translate = self.translator.translate(message)

        return message_translate
    
    def get_food(self, food):
        _food_details = dict()

        food_en = self.__translate_message(food).lower()
        url = f"{self.__get_url()}&ingr={food_en}"

        request = requests.get(url)
        response = request.json()

        for food in response['parsed']:
            food_details = food['food']
            if food_details['label'].lower() == food_en:
                food_details['nutrients'] = self.__parser_nutrients(food_details['nutrients'])
                _food_details['food'] = food_details

        return _food_details
    
    def __parser_nutrients(self, nutrients):
        nutrient_formated = dict()

        for nutrient in nutrients:
            nutrient_pt = self.__translate_message(
                                                    NTR_code[nutrient], 
                                                    target="pt"
                                                ).upper()
            nutrient_formated[nutrient_pt] = nutrients[nutrient]

        return nutrient_formated
