# https://stepik.org/lesson/594680/step/6?unit=589701

def get_value(nested_dicts, key, res=''):
    for elem, value in nested_dicts.items():
        if elem == key:
            return value
        elif isinstance(value, dict):
            res = get_value(value, key)
            if res is not None:
                return res