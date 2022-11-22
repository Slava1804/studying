# https://stepik.org/lesson/445985/step/7?unit=470426

s_numbers = [int(c) for c in input().split()]
s_numbers_2 = [int(c) for c in input().split()]

print(['NO', 'YES'][set(s_numbers) == set(s_numbers_2)])