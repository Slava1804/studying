# https://stepik.org/lesson/416757/step/5?auth=login&thread=solutions&unit=406265

n = int(input())
mat = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or i+j+1 == n:
            mat[i][j] = 1

[print(*c) for c in mat]