n = int(input())
s = n
t = ''
t1 = ''
while n != 0:
    s %= 2
    t += str(s)
    n //= 2
    s = n
for i in range(len(t) - 1, -1, -1):
    t1 += t[i]    
print(t1)
print(s)

