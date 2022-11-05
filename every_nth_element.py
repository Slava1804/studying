# https://stepik.org/lesson/416759/step/1?unit=406267

sym = input().split()
n = int(input())
mat = [[] for _ in range(n)]

for i in range(0, len(sym), n):
    s = sym[i:i+n]
    for j in range(len(s)):
        mat[j].append(s[j])

print(mat)