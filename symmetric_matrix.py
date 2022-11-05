# https://stepik.org/lesson/416759/step/5?unit=406267

n = int(input())
mat = [[int(c) for c in input().split()] for _ in range(n)]

def symm(list1, num):
    for i in range(num):
        for j in range(num):
            if list1[i][j] != list1[n-j-1][n-i-1]:
                return 'NO'
    
    return 'YES'

print(symm(mat, n))