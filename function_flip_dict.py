# https://stepik.org/lesson/590035/step/23?thread=solutions&unit=584967

from collections import defaultdict

def flip_dict(dict_of_lists: dict):
    result = defaultdict(list)

    for key, values in dict_of_lists.items():
        for value in values:
            result[value].append(key)

    return result