# https://stepik.org/lesson/669733/step/16?unit=667881

class Alphabet:
    def __init__(self, language) -> None:
        alphabet = {'en': 'abcdefghijklmnopqrstuvwxyz', 'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}
        self.letters = alphabet[language]
        self.index = -1
        self.length = len(alphabet[language])-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index != self.length:
            self.index += 1
            return self.letters[self.index]
        self.index = 0
        return self.letters[self.index]