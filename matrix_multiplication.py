# https://stepik.org/lesson/416756/step/10?unit=406264

n, m = [int(c) for c in input().split()]
mat_a = [[int(i) for i in input().split()] for _ in range(n)]
input()
m, k = [int(c) for c in input().split()]
mat_b = [[int(i) for i in input().split()] for _ in range(m)]
mat_c = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for c in range(m):
            mat_c[i][j] += mat_a[i][c] * mat_b[c][j]
            
[print(*c) for c in mat_c]