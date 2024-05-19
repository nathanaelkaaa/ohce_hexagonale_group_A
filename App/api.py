import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from Classes.Horloge import Horloge
from Classes.Langue import Langue
from Classes.AnalyseurDeChaine import AnalyseurDeChaine


app = Flask(__name__)

@app.route('/analyse', methods=['POST'])
def analyse():
    contenu = request.json['text']
    langue_code = request.headers.get('Accept-Language', None)
    langue = Langue('traductions.json', langue_code)
    horloge = Horloge()
    analyseur = AnalyseurDeChaine(langue, horloge)
    reponse = analyseur.analyser_chaine(contenu)
    return jsonify({"reponse": reponse})

if __name__ == '__main__':
    app.run(debug=True)
