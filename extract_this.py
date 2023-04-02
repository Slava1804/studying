# https://stepik.org/lesson/547172/step/21?unit=540798

from zipfile import ZipFile

def extract_this(zip_name, *args):
    with ZipFile(zip_name) as file:
        names = file.namelist()
        if not args:
            file.extractall()
        else:
            for f in args:
                file.extract(f.split('/')[-1])