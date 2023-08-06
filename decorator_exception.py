# https://stepik.org/lesson/640039/step/23?unit=636559


def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), 'Функция выполнилась без ошибок'
        except:
            return None, 'При вызове функции произошла ошибка'
    return wrapper