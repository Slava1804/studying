num = int(input())
mat = [(input().split()) for _ in range(num)]

res = sum([int(mat[i][i]) for i in range(num)])

print(res)