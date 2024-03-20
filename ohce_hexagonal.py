import os
import json
from datetime import datetime

DEFAULT_LANG = 'en'

def get_time():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 18:
        return "afternoon"
    else:
        return "evening"

def get_translation(language, key):
    try:
        with open('translations.json', 'r') as file:
            translations = json.load(file)
            return translations.get(language, {}).get(key, "")
    except FileNotFoundError:
        print("File not found.")
        return ""
    except json.JSONDecodeError:
        print("Error while reading JSON file.")
        return ""

def is_palindrome(user_input):
    return user_input == user_input[::-1]

def detect_language_os():
    lang = os.environ.get('LANG', 'en')[:2]
    return lang

def verify_language(lang):
    with open('translations.json', 'r') as file:
        translations = json.load(file)
    return lang if lang in translations else DEFAULT_LANG


def main():
    detect_lang = detect_language_os()
    language = verify_language(detect_lang)
    time_of_day = get_time()
    
    print(get_translation(language, time_of_day))
    print(get_translation(language, "intro"))
    
    while True:
        user_input = input("> ").strip()
        
        if user_input.lower() == "exit":
            print(get_translation(language, "exit"))
            break
        elif is_palindrome(user_input.replace(" ", "").lower()):
            print(get_translation(language, "is_palindrome"))
        else:
            print(user_input[::-1])

if __name__ == "__main__":
    main()
