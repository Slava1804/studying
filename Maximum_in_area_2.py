# https://stepik.org/lesson/416754/step/13?thread=solutions&unit=406262

num = int(input())
mat = []

for i in range(num):
    list1 = [int(i) for i in input().split()]
    mat.append(list1)

larg = mat[0][0]

for c in range(num):
    for k in range(num):
        if (c > k and c < num - 1 - k) or (c < k and c > num - 1 - k):
            if mat[c][k] > larg:
                larg = mat[c][k]
        elif mat[c][c] > larg:
            larg = mat[c][c]
        elif mat[c][num - c - 1] > larg:
            larg = mat[c][num - c - 1]

print(larg)