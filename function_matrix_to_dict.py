# https://stepik.org/lesson/655394/step/17?unit=652334


def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return dict(enumerate(matrix, 1))