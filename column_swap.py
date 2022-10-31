# https://stepik.org/lesson/416755/step/3?thread=solutions&unit=406263

n = int(input())
m = int(input())

mat = [[int(i) for i in input().split()] for _ in range(n)]
num = [int(j) for j in input().split()]
mat_copy = []

for k in num:
    mat_copy.append([mat[c][k] for c in range(n)])

mat_copy.reverse()
i = 0

for y in num:
    for h in range(n):
        for g in range(m):
            if g == y:
                mat[h][g] = mat_copy[i][h]
    i += 1

[print(*q, sep=' ') for q in mat]