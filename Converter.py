from os.path import exists
from random import randint

from pyperclip import copy

from Exceptions import LetterFileReadError


class Converter():
    def __init__(self):
        self.dictionary = dict()
        self.dictionaryFilePath = 'Letters.txt'
        self.curseRegister = True

        self.CreateDictionary()

    def CreateDictionary(self):
        if exists(self.dictionaryFilePath):
            self.CreateDictionaryFromFile(self.dictionaryFilePath)
        else:
            self.CreateDefaultDictionary()

    def CreateDictionaryFromFile(self, filename):
        with open(filename, 'r', encoding="utf8") as file:
            data = [x.strip() for x in file.read().split('\n') if not str.isspace(x) and len(x) > 0]

        for j in data:
            if " — " in j:
                itemContent = j.split(" — ")
            elif ' - ' in j:
                itemContent = j.split(' - ')
            else:
                raise LetterFileReadError
            if len(itemContent) == 2:
                replacingItems = itemContent[1].split(',')
                self.dictionary[itemContent[0]] = replacingItems

    def CreateDefaultDictionary(self):
        self.dictionary = {'А': ['Á', 'À', 'Ä', 'Â', 'Å', 'Ã', 'Ā', 'Ă', 'Ą', 'Æ'],
                           'а': ['á', 'à', 'ä', 'â', 'å', 'ã', 'ā', 'ă', 'ą'],
                           'б': ['ð'], 'В': ['ẞ', 'ß'],
                           'в': ['ẞ', 'ß'],
                           'г': ['ґ', 'ŕ'],
                           'Г': ['Ґ', 'Ğ'],
                           'Д': ['Ď', 'Ð', 'Đ'],
                           'д': ['ġ', 'ğ', 'ģ'],
                           'Е': ['É', 'È', 'Ê', 'Ě', 'Ē', 'Ę'],
                           'е': ['é', 'è', 'ê', 'ě', 'ē', 'ę'],
                           'з': ['Ž', 'ž'],
                           'и': ['ї', 'î', 'ú', 'ü', 'û', 'ů', 'ū', 'ų', '¡'],
                           'И': ['Î', 'Ü', 'Ū'],
                           'к': ['Ķ', 'ķ'],
                           'л': ['Ļ', 'Ĺ', 'Ł', 'ł'],
                           'н': ['Ħ'],
                           'О': ['Ó', 'Ö', 'Ô', 'Ő', 'Õ', 'Ō', 'Ø'],
                           'о': ['ó', 'ö', 'ô', 'ő', 'õ', 'ō', 'ø'],
                           'п': ['ń', 'ň', 'ñ', 'ņ', 'ħ'],
                           'р': ['þ', 'Þ'],
                           'С': ['Ć', 'Č', 'Ç'],
                           'с': ['ć', 'č', 'ç'],
                           'т': ['Ť', 'ť', 'Ț', 'ț', 'Ţ', 'ţ'],
                           'у': ['ý', 'ÿ'],
                           'У': ['Ÿ'],
                           'э': ['є'],
                           'Я': ['Ŕ', 'Ř']}

    def GetCursedLetter(self, letter):
        if self.curseRegister:
            if letter.lower() in self.dictionary.keys() and letter.upper() in self.dictionary.keys():
                options = *self.dictionary[letter.lower()], *self.dictionary[letter.upper()]
                return options[randint(0, len(options) - 1)]

        if letter in self.dictionary.keys():
            options = self.dictionary[letter]
            return options[randint(0, len(options) - 1)]

        letterRegisters = [letter.lower(), letter.upper()]
        if letterRegisters[0] in self.dictionary.keys():
            letter = letterRegisters[0]
        elif letterRegisters[1] in self.dictionary.keys():
            letter = letterRegisters[1]
        else:
            return letter
        options = self.dictionary[letter]
        return options[randint(0, len(options) - 1)]

    def GetCursedString(self, original):
        for letter in original:
            cursedLetter = self.GetCursedLetter(letter)
            original = original.replace(letter, cursedLetter, 1)

        return original

    def ChangeRegisterSensitivity(self):
        self.curseRegister = not self.curseRegister

    def copyTextToClipboard(self, text):
        copy(text)
