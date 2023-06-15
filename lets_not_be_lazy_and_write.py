# https://stepik.org/lesson/590120/step/17?thread=solutions&unit=585064

from collections import Counter

[print(f'{key}: {value}') for key, value in sorted(Counter(input().split(',')).items())]