# langue.py
from LangueManager import LanguageManager

# langue.py
import os
import json

class Langue:
    def __init__(self, translations_file, language_code):
        self.language_manager = LanguageManager(translations_file)
        self.language_code = language_code

    def detect_language_os(self):
        return os.environ.get('LANG', 'en')[:2]

    def saluer(self, moment):
        raise NotImplementedError

    def feliciter(self):
        raise NotImplementedError

    def acquitter(self, moment):
        raise NotImplementedError


# langue_en.py
class LangueTranslation(Langue):
    def saluer(self, moment):
        if 5 <= moment < 12:
            return self.language_manager.get_translation(self.language_code, 'morning')
        elif 12 <= moment < 18:
            return self.language_manager.get_translation(self.language_code, 'afternoon')
        else:
            return self.language_manager.get_translation(self.language_code, 'evening')

    def feliciter(self):
        return self.language_manager.get_translation(self.language_code, 'well_said')

    def acquitter(self):
        return self.language_manager.get_translation(self.language_code, 'goodbye')
