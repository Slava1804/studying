# https://stepik.org/lesson/416755/step/8?unit=406263

mat = [['.' for c in range(8)] for _ in range(8)]
sym = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
num = {'8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}
pos = input()
a, b = sym[pos[0]], num[pos[1]]
mat[b][a] = 'N'

for i in range(8):
    for j in range(8):
        inx = (b - j) * (a - i)
        if inx == 2 or inx == -2:
            mat[j][i] = '*'

[print(*k) for k in mat]