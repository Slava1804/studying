# https://stepik.org/lesson/547172/step/23?unit=540798

from zipfile import ZipFile

def conversion(num):
    if num < 1024:
        return f'{num} B'
    elif (num // 1024) < 1024:
        return f'{round(num / 1024)} KB'
    elif (num // (1024**2)) < 1024:
        return f'{round(num / (1024**2))} MB'
    elif (num // (1024**3)) < 1024:
        return f'{round(num / (1024**3))} GB'

with ZipFile('desktop.zip') as file:
    info = file.infolist()
    for inf in info:
        emp = inf.filename.count('/')
        name = inf.filename.split('/')
        if '' in name:
            print(f'{"  "*(emp-1)}{name[-2]}')
        else:
            print(f'{"  "*(len(name)-1)}{name[-1]} {conversion(inf.file_size)}')