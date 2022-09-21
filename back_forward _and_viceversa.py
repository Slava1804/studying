num_arr = [int(i) for i in input().split(' ')]
res_arr = []
while num_arr != []:
    sym = num_arr[:2]
    del num_arr[:2]
    res_arr.append(sym[::-1])
for i in range(len(res_arr)):
    print(* res_arr[i], end=' ')