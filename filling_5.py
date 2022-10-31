# https://stepik.org/lesson/416757/step/7?auth=login&thread=solutions&unit=406265

n, m = [int(c) for c in input().split()]
mat = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mat[i][j] = (i + j) % m+1

for c in mat:
    for k in range(m):
        print(str(c[k]).ljust(3), end=' ')
    print()        