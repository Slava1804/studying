# https://stepik.org/lesson/640040/step/22?unit=636560


import functools

def takes(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            elements = map(type, list(args)+list(kwargs.values()))
            if all(map(lambda x: x in types, elements)):
                return func(*args, **kwargs)
            raise TypeError
        return wrapper
    return decorator