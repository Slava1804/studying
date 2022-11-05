# https://stepik.org/lesson/416759/step/7?thread=solutions&unit=406267

tab = [['.'] * 8 for _ in range(8)]
s = input()
n, k = ord(s[0]) - 97, abs(int(s[1])-8)

for i in range(8):
    for j in range(8):
        tab[k][j] = '*'
        tab[i][n] = '*'
        if i + j == k + n:
            tab[i][j] = '*'
        if i - j == k - n:
            tab[i][j] = '*'          
        
tab[k][n] = 'Q'

for sym in tab:
    print(*sym, end='\n')