# main_console.py
from Horloge import Horloge
from Langue import Langue
from AnalyseurDeChaine import AnalyseurDeChaine


def main():
    langue = Langue('translations.json')  # Automatically detects language or uses English
    horloge = Horloge()
    analyseur = AnalyseurDeChaine(langue, horloge)

    while True:
        entree = input("Enter text ('exit' to quit): ")
        if entree.lower() == 'exit':
            print(langue.acquitter(horloge.get_heure_actuelle()))
            break
        print(analyseur.analyser_chaine(entree))

if __name__ == "__main__":
    main()
