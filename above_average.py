# https://stepik.org/lesson/416754/step/11?unit=406262

num = int(input())

for i in range(num):
    list1 = [int(i) for i in input().split()]
    s = sum(list1) / num
    t = 0
    for j in range(len(list1)):
        if list1[j] > s:
            t += 1
    print(t)