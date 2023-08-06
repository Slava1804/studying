# https://stepik.org/lesson/640039/step/19?unit=636559


def sandwich(func):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        obj = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return obj
    return wrapper