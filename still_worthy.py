# https://stepik.org/lesson/635441/step/16?thread=solutions&unit=631831

from collections import Counter
import sys

students = Counter()

for student in map(str.strip, sys.stdin):
    key, value = student.split()
    students[key] = int(value)

print(students.most_common()[-2][0])