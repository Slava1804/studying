# https://stepik.org/lesson/445985/step/4?unit=470426

n = int(input())
myset = set(input() for _ in range(n))
print(['OK', 'REPEAT'][input() in myset])
