# https://stepik.org/lesson/416759/step/2?unit=406267

n = int(input())
mat = [[int(c) for c in input().split()] for _ in range(n)]
res = []

for i in range(n):
    for j in range(n):
        if i >= n-1-j:
            res.append(mat[i][j])

print(max(res))