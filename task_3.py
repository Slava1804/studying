n = int(input())
a = 0
b = 0
c = 0
d = 0

while n != 0:
    a = n % 10
    b += a
    n //= 10
while b != 0:
    d = b % 10
    c += d
    b //= 10
print(c)