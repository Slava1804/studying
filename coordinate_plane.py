num_iter = int(input())
fir_qu = 0
sec_qu = 0
thi_qu = 0
fou_qu = 0
for _ in range(num_iter):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        continue
    else:
        if x < 0:
            if y > 0:
                sec_qu += 1
            else:
                thi_qu += 1
        else:
            if y > 0:
                fir_qu += 1
            else:
                fou_qu += 1
print('Первая четверть:', fir_qu)
print('Вторая четверть:', sec_qu)
print('Третья четверть:', thi_qu)
print('Четвертая четверть:', fou_qu)