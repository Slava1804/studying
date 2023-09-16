# https://stepik.org/lesson/669733/step/13?unit=667881

class CardDeck:
    def __init__(self) -> None:
        self.suits = ('пик', 'треф', 'бубен', 'червей')
        self.nominlal = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз')
        self.index_suits = 0
        self.index_nominal = -1
        self.counter = 52

    def __iter__(self):
        return self

    def __next__(self):
        if not self.counter:
            raise StopIteration
        if self.index_nominal > 11:
            self.index_suits += 1
            self.index_nominal = -1
        if self.index_suits > 3:
            self.index_suits = 0
        self.index_nominal += 1
        self.counter -= 1
        return f'{self.nominlal[self.index_nominal]} {self.suits[self.index_suits]}'