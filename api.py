from flask import Flask, request, jsonify
from Horloge import Horloge
from Langue import Langue # Assume this is a subclass of Langue tailored for English
from AnalyseurDeChaine import AnalyseurDeChaine

app = Flask(__name__)

@app.route('/analyse', methods=['POST'])
def analyse():
    content = request.json['text']
    lang_header = request.headers.get('Accept-Language', None)
    langue = Langue('translations.json', lang_header)
    horloge = Horloge()
    analyseur = AnalyseurDeChaine(langue, horloge)
    response = analyseur.analyser_chaine(content)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
