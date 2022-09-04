s = input()
t = 0
if s[0] == '7' and s[1] != '7':
    if s[1] == '-' and s[5] == '-' and s[9] == '-':
        m = s.split('-')
        s1 = ''.join(m)
        for i in range(len(s1)):
            if s1[i] in '0123456789':
                t += 1
            else:
                print('NO')
                break
            if t == len(s1):
                print('YES')
elif s[3] == '-' and s[7] == '-':
        m = s.split('-')
        s1 = ''.join(m)
        for i in range(len(s1)):
            if s1[i] in '0123456789':
                t += 1
            else:
                print('NO')
                break
            if t == len(s1):
                print('YES')
else:
    print('NO')