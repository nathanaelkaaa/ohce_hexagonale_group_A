import json

class Langue:
    def __init__(self, fichier_traduction, langue_code):
        self.traductions = self.charger_traductions(fichier_traduction)
        self.langue_code = langue_code

    def charger_traductions(self, chemin_fichier):
        with open(chemin_fichier, 'r') as file:
            traductions = json.load(file)
        return traductions

    def obtenir_traduction(self, language, key):
        return self.traductions.get(language, {}).get(key, "")

    def saluer(self, moment):
        if 5 <= moment < 12:
            return self.obtenir_traduction(self.langue_code, 'morning')
        elif 12 <= moment < 18:
            return self.obtenir_traduction(self.langue_code, 'afternoon')
        else:
            return self.obtenir_traduction(self.langue_code, 'evening')

    def feliciter(self):
        return self.obtenir_traduction(self.langue_code, 'is_palindrome')

    def acquitter(self):
        return self.obtenir_traduction(self.langue_code, 'exit')
