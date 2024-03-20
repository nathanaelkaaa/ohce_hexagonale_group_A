import os
from datetime import datetime

translation_dictionary = {
    "fr": {
        "intro" : "Entrez du texte ici. 'exit' pour quitter",
        "exit" : "Au revoir",
        "morning" : "Bonjour",
        "afternoon" : "Bon après-midi",
        "evening" : "Bonsoir",
        "is_palindrome" : "Bien dit !"
    },
    "en": {
        "intro" : "Enter text here. 'exit' to quit",
        "exit" : "Goodbye",
        "morning" : "Good morning",
        "afternoon" : "Good afternoon",
        "evening" : "Good evening",
        "is_palindrome" : "Well said!"
    }
}

def get_time():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 18:
        return "afternoon"
    else:
        return "evening"

def get_translation(language, key):
    return translation_dictionary[language].get(key, "")

def is_palindrome(s):
    return s == s[::-1]

def detect_language_os():
    # Obtenir la langue depuis la variable d'environnement et utilisation de l'anglais, 'en', par défaut
    lang = os.environ.get('LANG', 'en')[:2]
    return lang if lang in translation_dictionary else "en"

def main():
    language = detect_language_os()
    print(get_translation(language, "intro"))
    
    greeted = False
    
    while True:
        user_input = input("> ").strip()
        
        if not greeted:
            time_of_day = get_time()
            print(get_translation(language, time_of_day))
            greeted = True

        if user_input.lower() == "exit":
            print(get_translation(language, "exit"))
            break
        elif is_palindrome(user_input.replace(" ", "").lower()):
            print(get_translation(language, "is_palindrome"))
        else:
            print(user_input[::-1])

if __name__ == "__main__":
    main()
