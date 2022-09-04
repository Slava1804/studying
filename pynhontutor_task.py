n = int(input())
a = n
b = n
b = b % 60
if a > 1440:
    while a > 1440:
        a = a - 1440
        if a < 1440:
            a = a // 60
else:
    a = a // 60
    if a == 24:
        a = 0
print(a, b)
