# https://stepik.org/lesson/416755/step/2?thread=solutions&unit=406263

n = int(input())
m = int(input())

mat = []

for _ in range(n):
    s = input().split()
    s = [int(c) for c in s]
    mat.append(s)

i = 0
larg = -1000

for c in mat:
    if max(c) > larg:
        st = i
        s = c.index(max(c))
        larg = max(c)
    elif max(c) == larg and i < st:
        st = i
        s = c.index(max(c))
    elif i == st and c.index(max(c)) < s:
        st = i
        s = c.index(max(c))

    i += 1

print(st, s)