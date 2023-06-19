# https://stepik.org/lesson/635441/step/14?thread=solutions&unit=631831

from collections import Counter

words = Counter(input().lower().split()).most_common()
num = words[0][1]
print(max(n[0] for n in words if n[1] == num))