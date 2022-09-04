c = input()
j = 0
mx = ''
for i in range(1, len(c)):
    s = c.count(c[i])
    t = c.count(c[j])
    if c[i] == c[j]:
        if s >= t:
            mx = c[i] 
        continue
    else:
        if s >= t:
            mx = c[i] 
    j += 1
print(mx)       