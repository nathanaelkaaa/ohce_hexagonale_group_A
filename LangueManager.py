# language_manager.py
import json

class LanguageManager:
    def __init__(self, filepath):
        self.translations = self.load_translations(filepath)

    def load_translations(self, filepath):
        with open(filepath, 'r') as file:
            translations = json.load(file)
        return translations

    def get_translation(self, language, key):
        return self.translations.get(language, {}).get(key, "")
