# https://stepik.org/lesson/743710/step/14?thread=solutions&unit=745474

from collections import ChainMap

def deep_update(chainmap, key, value):
    keys = list(map(lambda x: x, chainmap))

    if key not in keys:
        chainmap[key] = value
    else:
        for d in chainmap.maps:
            if key in d:
                d[key] = value