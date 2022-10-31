# https://stepik.org/lesson/416757/step/2?unit=406265

n = int(input())
mat = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i + j + 1 == n:
            mat[i][j] = 1
        elif ((i > j) and
              (i > n - 1 - j)) or ((i < j) and
                                   (i > n - 1 - j)) or j == i and i >= n / 2:
            mat[i][j] = 2

[print(*k, end='\n') for k in mat]
