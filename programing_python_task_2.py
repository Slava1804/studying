# 1

'''mfpg = float(input())
print(mpg * 3.785451)'''

# 2

'''s = int(input())
coins = [200, 100, 25, 10, 5, 1]

for i in range(len(coins)):
    print(s // coins[i], coins[i], 'центовых монет')
    s %= coins[i]'''

# 3

'''a = float(input())
b = float(input())

print((a / 12) * 2.54 + b * 2.54)'''

# 4

'''di = float(input())

print((di / 12) * 2,54,
      di / 3,
      di / 5280, sep='\n')'''

# 5

'''from math import pi 

r = int(input())

print(pi * r ** 2, 4 * pi * r ** 2)'''

# 6

'''from math import pi

r = int(input())
h = int(input())

print(round((pi * r ** 2) * h, 1))'''

# 7

'''m = int(input())

print((2*9.8*m)**0.5)'''

# 8

'''b = int(input())
h = int(input())

print((b * 2) / 2)'''

# 9

'''from math import pi, tan

s = int(input())
n = int(input())

print((n * s**2) / (4 * tan(pi / n)))'''

# 10

'''list1 = [86400, 3600, 60, 1]
res = 0

for i in range(4):
    t = int(input()) * list1[i]
    res += t

print(res)'''