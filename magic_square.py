# https://stepik.org/lesson/416755/step/9?unit=406263


def magic_square(mat, num):
    for c in mat:
        if 0 in c:
            return 'NO'

    z = 0
    h = 0
    q = []
    for i in range(num):
        x, y = 0, 0
        z += mat[i][i]
        for j in range(num):
            if mat[i][j] > n**2:
                return 'NO'
            if i + j + 1 == n:
                h += mat[i][j]
            x += mat[i][j]
            y += mat[j][i]
            q.append(mat[i][j])
        if x != y:
            return 'NO'
    if len(set(q)) != n**2:
        return 'NO'
    if z == h:
        return 'YES'

    return 'NO'


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

print(magic_square(matrix, n))