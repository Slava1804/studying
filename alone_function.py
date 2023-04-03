# https://stepik.org/lesson/584474/step/13?unit=579234

import pickle
import sys

name_file, *other = [c.strip() for c in sys.stdin]
with open(name_file, 'rb') as file:
    print(pickle.load(file)(*other))