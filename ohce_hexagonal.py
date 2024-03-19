from datetime import datetime
from langdetect import detect, LangDetectException


welcome_messages = {
    "morning": {"fr": "Bonjour", "en": "Good morning"},
    "afternoon": {"fr": "Bon après-midi", "en": "Good afternoon"},
    "evening": {"fr": "Bonsoir", "en": "Good evening"}
}

def get_time():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 18:
        return "afternoon"
    else:
        return "evening"

def get_welcome(language):
    time_of_day = get_time()
    return welcome_messages[time_of_day].get(language, "Hello")

def get_out(language):
    return {"fr": "Au revoir", "en": "Goodbye"}.get(language, "Goodbye")

def is_palindrome(s):
    return s == s[::-1]

def detect_language(text):
    try:
        return detect(text) if len(text) > 3 else "en"
    except LangDetectException:
        return "en"

def main():
    print("Entrez du texte ici. 'exit' pour quitter")
    
    language = "en"  
    greeted = False
    
    while True:
        user_input = input("> ").strip()
        
        if not greeted:
            language = detect_language(user_input)
            print(get_welcome(language))
            greeted = True

        if user_input.lower() == "exit":
            print(get_out(language))
            break
        elif is_palindrome(user_input.replace(" ", "").lower()):
            print({"fr": "Bien dit !", "en": "Well said!"}.get(language, "Well said!"))
        else:
            print(user_input[::-1])

if __name__ == "__main__":
    main()
