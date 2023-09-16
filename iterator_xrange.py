# https://stepik.org/lesson/669733/step/17?unit=667881

class Xrange:
    def __init__(self, start, end, step=1) -> None:
        self.start = start-step
        self.end = end-step
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.start >= self.end:
                raise StopIteration
        else:
            if self.start <= self.end:
                raise StopIteration
        self.start += self.step
        return self.start