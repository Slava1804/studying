# https://stepik.org/lesson/416757/step/8?auth=login&thread=solutions&unit=406265

n, m = [int(c) for c in input().split()]
mat = []
start = 1
end = m

for i in range(n):
    list1 = list(range(start, end + 1))
    start = end + 1
    end += m
    if i % 2 == 0:
        mat.append(list1)
    else:
        list1.reverse()
        mat.append(list1)
    
for c in mat:
    for k in range(m):
        print(str(c[k]).ljust(3), end=' ')
    print()        