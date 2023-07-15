# https://stepik.org/lesson/594680/step/7?unit=589701

def get_all_values(nested_dicts, key):
    res = set()
    for elem, value in nested_dicts.items():
        if elem == key:
            res.add(value)
        elif isinstance(value, dict):
            res.update(get_all_values(value, key))
    return res