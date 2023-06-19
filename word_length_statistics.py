# https://stepik.org/lesson/635441/step/15?unit=631831

from collections import Counter

words_len = Counter([len(c) for c in input().split()])
keys = list(words_len.keys())

for key, value in sorted(words_len.items(), key=lambda x: (x[1], keys.index(x[0]))):
    print(f'Слов длины {key}: {value}')