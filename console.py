# console.py
import json
from Horloge import Horloge
import os
from Langue import Langue
from AnalyseurDeChaine import AnalyseurDeChaine


def main():
    langue_code = os.environ.get('LANG', 'en')[:2]
    langue = Langue('traductions.json', langue_code)
    horloge = Horloge()
    analyseur = AnalyseurDeChaine(langue, horloge)
    
    heure = horloge.obtenir_heure_actuelle()
    salutation = langue.saluer(heure)
    intro = langue.obtenir_traduction(langue_code, 'intro')
    acquitter = langue.acquitter()
    
    print(f"{salutation}")

    while True:
        chaine = input(f"{intro} : ").strip()
        if chaine.lower() == 'exit':
            print(f"{acquitter}")
            break

        resultat = analyseur.analyser_chaine(chaine)
        print(f"{resultat}")

if __name__ == '__main__':
    main()
