# https://stepik.org/lesson/416756/step/11?unit=406264

n = int(input())
mat_a = [[int(c) for c in input().split()] for _ in range(n)]
mat_copy = [c for c in mat_a]
mat_b = [[0] * n for _ in range(n)]
m = int(input())

for _ in range(1, m):
    for i in range(n):
        for j in range(n):
            for c in range(n):
                mat_b[i][j] += mat_a[i][c] * mat_copy[c][j]
    mat_copy = mat_b
    mat_b = [[0] * n for _ in range(n)]

[print(*c) for c in mat_copy]
