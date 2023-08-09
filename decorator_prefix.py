# https://stepik.org/lesson/640040/step/17?unit=636560


import functools

def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if to_the_end:
                return func(*args, **kwargs)+string
            return string+func(*args, **kwargs)
        return wrapper
    return decorator