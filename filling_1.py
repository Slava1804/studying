# https://stepik.org/lesson/416757/step/3?thread=solutions&unit=406265

n, m = [int(k) for k in input().split()]
mat = []
start = 1
end = m

for _ in range(n):
    list1 = list(range(start, end + 1))
    start = end + 1
    end += m
    mat.append(list1)

[print(*c) for c in mat]