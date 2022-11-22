# https://stepik.org/lesson/445985/step/9?unit=470426

n1, n2 = [int(input()) for _ in range(2)]
set1 = {input() for _ in range(n1)}
set2 = {input() for _ in range(n2)}
res = set1 ^ set2
(print(len(res)) if len(res) > 0 else print('NO'))