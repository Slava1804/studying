# https://stepik.org/lesson/445985/step/8?unit=470426

n1, n2 = [int(input()) for _ in range(2)]
set1 = {input() for _ in range(n1)}
set2 = {input() for _ in range(n2)}
print(len(set1 - set2))
