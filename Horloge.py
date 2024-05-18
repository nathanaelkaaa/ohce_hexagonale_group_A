# horloge_systeme.py
from datetime import datetime

class Horloge():
    def obtenir_heure_actuelle(self):
        return datetime.now().hour