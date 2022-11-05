# https://stepik.org/lesson/416759/step/4?unit=406267

n = int(input())
mat = [['.'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or i+j+1 == n or j == n // 2 or i == n // 2:
            mat[i][j] = '*'

for row in mat:
    print(*row)