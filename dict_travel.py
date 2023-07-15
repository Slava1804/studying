# https://stepik.org/lesson/594680/step/8?unit=589701

def dict_travel(nested_dicts, st=''):
    for key, value in sorted(nested_dicts.items()):
        if isinstance(value, dict):
            dict_travel(value, st+f'{key}.')
        else:
            print(f'{st}{key}: {value}')