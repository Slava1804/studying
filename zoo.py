# https://stepik.org/lesson/634670/step/22?thread=solutions&unit=630932

from collections import ChainMap
import json

with open('zoo.json', encoding='utf-8') as file:
    data = json.load(file)

    print(sum(ChainMap(*data).values()))