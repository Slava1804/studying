# https://stepik.org/lesson/547172/step/17?unit=540798

from zipfile import ZipFile

with ZipFile('workbook.zip') as file:
    info = file.infolist()
    result = [f.filename.split('/')[-1] for f in info if f.date_time > (2021, 11, 30, 14, 22, 0) and not f.is_dir()]
    result.sort()

    print(*result, sep='\n')