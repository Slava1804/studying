# https://stepik.org/lesson/416759/step/8?thread=solutions&unit=406267

n = int(input())
mat = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j] = abs(i-j)

for sym in mat:
    print(*sym, end='\n')