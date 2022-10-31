# https://stepik.org/lesson/416757/step/4?auth=login&unit=406265

n, m = [int(k) for k in input().split()]
mat = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mat[i][j] = j * n + 1 + i

[print(*c) for c in mat]