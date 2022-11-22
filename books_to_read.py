# https://stepik.org/lesson/445985/step/5?unit=470426

n, n2 = [int(input()) for _ in range(2)]
set_list = {input() for _ in range(n)}

for _ in range(n2):
    if input() in set_list:
        print('YES')
    else:
        print('NO')