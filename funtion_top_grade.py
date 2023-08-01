# https://stepik.org/lesson/640039/step/1?unit=636559


def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    grades['top_grade'] = max(grades.pop('grades'))
    return grades