# https://stepik.org/lesson/590120/step/18?thread=solutions&unit=585064

from collections import Counter

prices = Counter(input().split(','))
max_space = max(map(len, prices))

for item in sorted(prices):
    sum_item = sum(ord(c) for c in item if c != ' ')
    count = prices[item]
    print(f'{item}{(max_space-len(item))*" "}: {sum_item} UC x {count} = {sum_item * count} UC')