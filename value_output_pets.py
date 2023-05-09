# https://stepik.org/lesson/740203/step/10?unit=741843

from collections import namedtuple
import pickle

with open('data.pkl', 'rb') as file:
    Animal = namedtuple('Animal', 'name family sex color')
    obj = pickle.load(file)
    pets = map(lambda x: 'name: {}\nfamily: {}\nsex: {}\ncolor: {}'.format(*Animal(*x)), obj)

    print(*pets, sep='\n\n')