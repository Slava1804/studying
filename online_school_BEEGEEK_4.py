# https://stepik.org/lesson/445985/step/10?unit=470426

s1 = {c for c in input().split()}
s2= {c for c in input().split()}
print(*sorted(s1 | s2))