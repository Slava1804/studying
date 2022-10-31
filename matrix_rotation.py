# https://stepik.org/lesson/416755/step/7?thread=solutions&unit=406263

n = int(input())
mat = [[int(i) for i in input().split()] for _ in range(n)]

for k in range(n):
    for c in range(n):
        print(mat[n-c-1][k], end=' ')
    print()