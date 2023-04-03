# https://stepik.org/lesson/584474/step/15?unit=579234

import pickle

name, num = input(), int(input())

with open(name, 'rb') as file:
    obj = pickle.load(file)
    lst = [i for i in obj if type(i) == int] or [0]
    res = sum(lst) if type(obj) == dict else max(lst)*min(lst)
    print(['Контрольные суммы не совпадают', 'Контрольные суммы совпадают'][res == num])