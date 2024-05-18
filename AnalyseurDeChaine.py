from Langue import Langue
from Horloge import Horloge
class AnalyseurDeChaine:
    def __init__(self, langue: Langue, horloge: Horloge):
        self.langue = langue 
        self.horloge = horloge

    def est_palindrome(self, chaine):
        return chaine == chaine[::-1]

    def analyser_chaine(self, chaine):
        heure = self.horloge.obtenir_heure_actuelle()
        salutation = self.langue.saluer(heure)

        if self.est_palindrome(chaine):
            return f"{salutation}, {chaine[::-1]}, {self.langue.feliciter()}, {self.langue.acquitter()}"
        else:
            return f"{salutation}, {chaine[::-1]}, {self.langue.acquitter()}"
