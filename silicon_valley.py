# https://stepik.org/lesson/415554/step/10?thread=solutions&unit=405083

arr_words = [input() for _ in range(int(input()))]
res = []
for i in range(len(arr_words)):
    s = arr_words[i]
    for j in range(len(s)):
        if s[j] not in 'anton':
            s = s.replace(s[j], '_')
    s = s.replace('_', '')
    if s == 'anton':
        res.append(i+1)
    else:
        end_s = s.rfind('n')
        start_s = s.rfind('a')
        s = s[start_s:end_s+1]
        s_arr = [i for i in s]
        for c in range(len(s_arr)):
            if s_arr.count(s_arr[c]) > 1 and s_arr[c] != 'n':
                s_arr.insert(c, '_')
                del s_arr[c+1]
        if len(s_arr) > 3:
            res_s = ''.join(s_arr).replace('_', '')
            res_s = res_s[0:2] + res_s[2:len(res_s)-1].replace('n', '') + res_s[-1]
            if res_s == 'anton':
                res.append(i+1)

print(* res)