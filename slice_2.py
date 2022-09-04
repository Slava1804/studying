c = input()
if len(c) % 2 != 0:
    a = c[:(len(c) + 2) // 2]
    b = c[(len(c) + 2) // 2:]
else:
    a = c[:(len(c) + 1) // 2]
    b = c[(len(c) + 1) // 2:]
t = b + a
print(t)