import os
import json
from datetime import datetime

DEFAULT_LANG = 'en'

def load_translations():
    with open('translations.json', 'r') as file:
        translations = json.load(file)
    return translations

def get_current_hour():
    return datetime.now().hour

def is_morning(hour):
    return 5 <= hour < 12

def is_afternoon(hour):
    return 12 <= hour < 18

def get_time():
    hour = get_current_hour()
    return "morning" if is_morning(hour) else "afternoon" if is_afternoon(hour) else "evening"

def find_translation(translations, language, key):
    return translations.get(language, {}).get(key, "")

def get_translation(translations, language, key):
    try:
        return find_translation(translations, language, key)
    except FileNotFoundError:
        print("File not found.")
        return ""
    except json.JSONDecodeError:
        print("Error while reading JSON file.")
        return ""

def detect_language_os():
    return os.environ.get('LANG', 'en')[:2]

def format_language(lang):
    return lang[:2]

def verify_language(lang, translations):
    return lang if lang in translations else DEFAULT_LANG

def get_language(translations):
    lang = detect_language_os()
    lang = format_language(lang)
    lang = verify_language(lang, translations)
    return lang

def inverse(string):
    return string[::-1]

def is_palindrome(user_input):
    return user_input == inverse(user_input)

def get_clean_input(prompt="> "):
    return input(prompt).strip()

def main():
    translations = load_translations()
    lang = get_language(translations)
    time_of_day = get_time()
    
    print(get_translation(translations, lang, time_of_day))
    print(get_translation(translations, lang, "intro"))
    
    while True:
        user_input = get_clean_input()
        
        if user_input.lower() == "exit":
            print(get_translation(translations, lang, "exit"))
            break
        elif is_palindrome(user_input.replace(" ", "").lower()):
            print(get_translation(translations, lang, "is_palindrome"))
        else:
            print(inverse(user_input))

if __name__ == "__main__":
    main()
