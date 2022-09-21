s = input().split()
arr = []
for i in s:
    if i in arr:
        continue
    else:
        arr.append(i)
print(len(arr))