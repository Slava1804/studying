from math import factorial

def pascal(n):
    list1 = []
    for j in range(n+1):
            res = factorial(n) / (factorial(j) * (factorial((n-j))))
            list1.append(int(res))
    return list1

num = int(input())
res_list = []

for i in range(num+1):
    res_list.append(pascal(i))
    
print(res_list[num])    