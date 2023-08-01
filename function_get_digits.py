# https://stepik.org/lesson/655394/step/14?unit=652334


def get_digits(number: int | float) -> list[int]:
    return list(map(int, str(number).replace('.', '')))