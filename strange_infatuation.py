# https://stepik.org/lesson/445985/step/6?unit=470426

set1 = {int(c) for c in input().split()}
set2 = {int(c) for c in input().split()}

if not set1.isdisjoint(set2):
    print(*sorted(set1 & set2, reverse=True))
else:
    print('BAD DAY')