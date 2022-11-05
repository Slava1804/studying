# https://stepik.org/lesson/416759/step/3?unit=406267

n = int(input())
mat = [[int(c) for c in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(n):
        print(mat[j][i], end=' ')
    print()