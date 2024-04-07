# -*- coding: utf-8 -*-


from flask import Flask, request, jsonify
from datetime import datetime
from dict import trad

app = Flask(__name__)

traductions=trad()

def get_salutation():
    heure_actuelle = datetime.now().hour
    if 5 <= heure_actuelle < 12:
        return 'morning'
    elif 12 <= heure_actuelle < 18:
        return 'afternoon'
    else:
        return 'evening'

def get_langue():
    langue = request.headers.get('Accept-Language', 'en').split(',')[0].split('-')[0]
    return langue if langue in traductions else 'en'

def est_un_palindrome(texte):
    return texte == texte[::-1]

def traiter_texte(texte, langue):
    salutation_key = get_salutation()
    salutation = traductions[langue][salutation_key]
    if est_un_palindrome(texte):
        return f"{salutation}, {traductions[langue]['well_said']}"
    else:
        return f"{salutation}, {texte[::-1]}"

@app.route('/check', methods=['POST'])
def check_text():
    langue = get_langue()  
    data = request.json
    texte = data.get('texte', '')
    resultat = traiter_texte(texte, langue)
    return jsonify({"reponse": resultat}), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
