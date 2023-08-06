# https://stepik.org/lesson/640039/step/21?unit=636559


def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper