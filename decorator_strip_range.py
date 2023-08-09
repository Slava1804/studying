# https://stepik.org/lesson/640040/step/20?unit=636560


import functools

def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            val = func(*args, **kwargs)
            return val[:start]+char*(min(end, len(val))-start)+val[end:]
        return wrapper
    return decorator