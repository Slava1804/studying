# https://stepik.org/lesson/635441/step/20?thread=solutions&unit=631831

from collections import Counter

def print_bar_chart(data, mark):
    count = Counter(data)
    space = len(max(data, key=len))

    for key, value in count.most_common():
        print(f'{key.ljust(space)} |{mark*value}')