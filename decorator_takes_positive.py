# https://stepik.org/lesson/640039/step/24?unit=636559


def takes_positive(func):
    def wrapper(*args, **kwargs):
        elements = list(args)+list(kwargs.values())
        if not all(map(lambda x: isinstance(x, int), elements)):
            raise TypeError
        elif not all(map(lambda x: isinstance(x, int) and x>0, elements)):
            raise ValueError
        return func(*args, **kwargs)
    return wrapper