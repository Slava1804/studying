n = int(input())
m = []
m1 = []
m2 = []
t = 0
for _ in range(n):
    c = input()
    m.append(c)
k = int(input())
for _ in range(k):
    c = input()
    m1.append(c)
for i in range(len(m)):
    for j in range(len(m1)):
        if m1[j].lower() in m[i].lower():
            t += 1
        if t == k:
            m2.append(m[i])
            t = 0
    t = 0
print(* m2, sep='\n')