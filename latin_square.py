# https://stepik.org/lesson/416759/step/6?unit=406267

n = int(input())
mat = [[int(c) for c in input().split()] for _ in range(n)]
num = list(range(1, n+1))
mat_tr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        mat_tr[i][j] = mat[j][i]

def lat_square(list_mat, list_num, a):

    for i in range(a):
        for j in range(a):
            if len(set(list_mat[i])) != a:
                return False
            elif list_num[j] not in list_mat[i]:
                return False

    return True

if lat_square(mat, num, n) and lat_square(mat_tr, num, n):
    print('YES')
else:
    print('NO')