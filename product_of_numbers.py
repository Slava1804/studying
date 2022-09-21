def pr_num(arr):
    flag = False
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            elif arr[i] * arr[j] == pr:
                flag = True
        if flag:
            return 'ДА'
    return 'НЕТ'

n = int(input())
arr_num = [int(input()) for _ in range(n)]
pr = int(input())
print(pr_num(arr_num))