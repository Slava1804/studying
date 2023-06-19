# https://stepik.org/lesson/635441/step/17?unit=631831

from collections import Counter

data = Counter(
    'aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi'
)

data.min_values = lambda: [(key, value) for key, value in data.items() if value == min(data.values())]
data.max_values = lambda: [(key, value) for key, value in data.items() if value == max(data.values())]