# https://stepik.org/lesson/743710/step/13?unit=745474

from collections import ChainMap

def get_all_values(chainmap: ChainMap, key) -> set:
    return {c[key] for c in chainmap.maps if key in c}
