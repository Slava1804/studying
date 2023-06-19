# https://stepik.org/lesson/635441/step/13?thread=solutions&unit=631831

from collections import Counter

words = Counter([c.lower() for c in input().split()]).most_common()[::-1]
num = words[0][1]
print(*sorted(n[0] for n in words if n[1] == num), sep=', ')