# https://stepik.org/lesson/640040/step/24?unit=636560


import functools

def ignore_exception(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as error:
                if type(error) in types:
                    print(f'Исключение {type(error).__name__} обработано')
                else:
                    raise error
        return wrapper
    return decorator