num = int(input())
mat = []

for i in range(num):
    list1 = [int(i) for i in input().split()]
    mat.append(list1)
    
larg = mat[0][0]

one_q = 0
two_q = 0
three_q = 0
four_q = 0 

for c in range(num):
    for k in range(num):
        if (c < k and c < num-1-k):
            one_q += mat[c][k]
        elif (c < k and c > num-1-k):
            two_q += mat[c][k]
        elif (c > k and c > num-1-k):
            three_q += mat[c][k]
        elif (c > k and c < num-1-k):
            four_q += mat[c][k]

print('Верхняя четверть:', one_q)
print('Правая четверть:', two_q)
print('Нижняя четверть:', three_q)
print('Левая четверть:', four_q)