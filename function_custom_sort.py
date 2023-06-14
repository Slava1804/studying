# https://stepik.org/lesson/634520/step/20?unit=630783

from collections import OrderedDict

def custom_sort(ordered_dict: OrderedDict, by_values=False):
    if not by_values:
        for key in sorted(ordered_dict):
            ordered_dict.move_to_end(key)
    else:
        for key in sorted(ordered_dict, key=lambda x: ordered_dict[x]):
            ordered_dict.move_to_end(key)