# https://stepik.org/lesson/640039/step/20?unit=636559


def new_print(func):
    def wrapper(*args, **kwargs):
        kwargs = {key: value.upper() for key, value in kwargs.items()}
        args = map(lambda x: x.upper() if isinstance(x, str) else x, args)
        return func(*args, **kwargs)
    return wrapper

print = new_print(print)