# https://stepik.org/lesson/547172/step/18?unit=540798

from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as file:
    info = file.infolist()
    result = []

    for inf in info:
        if not inf.is_dir():
            res = []
            res.append(f'{inf.filename.split("/")[-1]}')
            dat = datetime(*inf.date_time)
            res.append(f'  Дата модификации файла: {dat.strftime("%Y-%m-%d %H:%M:%S")}')
            res.append(f'  Объем исходного файла: {inf.file_size} байт(а)')
            res.append(f'  Объем сжатого файла: {inf.compress_size} байт(а)')
            result.append(res)

    result.sort(key=lambda x: x[0])
    for i in range(len(result)):
        print(*result[i], sep='\n')
        if i != len(result)-1:
            print()