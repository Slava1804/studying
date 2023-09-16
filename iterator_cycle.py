# https://stepik.org/lesson/669733/step/14?unit=667881

class Cycle:
    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.length = len(iterable)-1
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index != self.length:
            self.index += 1
            return self.iterable[self.index]
        self.index = 0
        return self.iterable[self.index]