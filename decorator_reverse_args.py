# https://stepik.org/lesson/640039/step/22?unit=636559


def reverse_args(func):
    def wrapper(*args, **kwargs):
        args = args[::-1]
        return func(*args, **kwargs)
    return wrapper