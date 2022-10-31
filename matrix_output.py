# https://stepik.org/lesson/416754/step/9?unit=406262

n = int(input())
m = int(input())
mat = []

for i in range(n):
    list1 = []
    for j in range(m):
        list1.append(input())
    mat.append(list1)

[print(* c) for c in mat]
print()

for c in range(m):
    for k in range(n):
        print(mat[k][c], end=' ')
    print()