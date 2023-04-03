# https://stepik.org/lesson/584474/step/14?unit=579234

import pickle

def filter_dump(filename, objects, typename):
    with open(filename, 'wb') as file:
        pickle.dump([el for el in objects if isinstance(el, typename)], file)