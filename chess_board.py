# https://stepik.org/lesson/416757/step/1?thread=solutions&unit=406265

n, m  = input().split()
mat = []

for i in range(int(n)):
    list1 = []
    for j in range(int(m)):
        if (i + j) % 2 == 0:
            list1.append('.')
        elif (i + j) % 2 != 0:
            list1.append('*')
    mat.append(list1)
    
[print(*c) for c in mat]