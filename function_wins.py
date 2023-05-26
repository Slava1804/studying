# https://stepik.org/lesson/590035/step/22?unit=584967

from collections import defaultdict

def wins(pairs):
    result = defaultdict(set)

    for winner, loser in pairs:
        result[winner].add(loser)

    return result