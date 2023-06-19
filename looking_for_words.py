# https://stepik.org/lesson/635441/step/12?unit=631831

from collections import Counter

words = Counter([c.lower() for c in input().split()])

print(words.most_common(1)[0][0])