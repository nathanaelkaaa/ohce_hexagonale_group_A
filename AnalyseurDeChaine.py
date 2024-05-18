# analyseur_de_chaine.py
class AnalyseurDeChaine:
    def __init__(self, langue, horloge):
        self.langue = langue
        self.horloge = horloge

    def est_palindrome(self, chaine):
        return chaine == chaine[::-1]

    def analyser_chaine(self, chaine):
        heure = self.horloge.get_heure_actuelle()
        salutation = self.langue.saluer(heure)
        acquittement = self.langue.acquitter(heure)
        if self.est_palindrome(chaine):
            return f"{salutation} {chaine} {self.langue.feliciter()} {acquittement}"
        else:
            return f"{salutation} {chaine[::-1]} {acquittement}"
