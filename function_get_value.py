# https://stepik.org/lesson/743710/step/15?thread=solutions&unit=745474

from collections import ChainMap

def get_value(chainmap: ChainMap, key, from_left=True):
        if not from_left:
            chainmap.maps.reverse()
        return chainmap.get(key)
