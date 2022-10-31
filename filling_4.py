# https://stepik.org/lesson/416757/step/6?auth=login&unit=406265

n = int(input())
mat = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i > j and i < n - 1 - j or i < j and i > n -1 - j:
            mat[i][j] = 0
        else:
            mat[i][j] = 1

for c in mat:
    for k in range(n):
        print(str(c[k]).ljust(3), end=' ')
    print()