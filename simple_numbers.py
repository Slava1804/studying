# На вход программе подается два натуральных числа aa и bb (a < ba< b).
# Напишите программу, которая находит все простые числа от aa до bb включительно.

a = int(input())
b = int(input())

for i in range(a, b + 1):
    t = 0
    for j in range(1, i + 1):
        if i % j == 0:
            t += 1
    if t == 2:
        print(i)