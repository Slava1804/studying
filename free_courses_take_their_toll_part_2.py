# https://stepik.org/lesson/635441/step/22?thread=solutions&unit=631831

from  collections import Counter

books, n = Counter(input().split()), int(input())
result = Counter()

for _ in range(n):
    book, price = input().split()
    if books[book] > 0:
        price = int(price)
        result[book] += price
        books[book] -= 1

print(result.total())