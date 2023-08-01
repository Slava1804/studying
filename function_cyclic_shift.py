# https://stepik.org/lesson/655394/step/16?unit=652334


from collections import deque

def cyclic_shift(numbers: list[int | float], step: int) -> None:
    res = deque(numbers)
    res.rotate(step)
    numbers[:] = list(res)