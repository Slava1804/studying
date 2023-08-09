# https://stepik.org/lesson/640040/step/23?unit=636560


import functools

def add_attrs(**attrs):
    def decorator(func):
        for name, value in attrs.items():
            func.__dict__[name] = value
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator