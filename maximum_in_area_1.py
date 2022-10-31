# https://stepik.org/lesson/416754/step/12?thread=solutions&unit=406262

num = int(input())
m = -1000

for i in range(num):
    list1 = [int(i) for i in input().split()]
    for j in range(i+1):
        if list1[j] > m:
            m = list1[j]

print(m)