# https://stepik.org/lesson/669733/step/15?unit=667881

from random import randint

class RandomNumbers:
    def __init__(self, left, right, n) -> None:
        self.left = left
        self.right = right
        self.n = n
        self.stop = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.stop > self.n:
            raise StopIteration
        self.stop += 1
        return randint(self.left, self.right)