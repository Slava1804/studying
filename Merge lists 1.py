def merge(list1, list2):
    m = sorted(list1 + list2)
    return m

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))