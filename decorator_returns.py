# https://stepik.org/lesson/640040/step/21?unit=636560


import functools

def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            val = func(*args, **kwargs)
            if isinstance(val, datatype):
                return val
            raise TypeError
        return wrapper
    return decorator