# https://stepik.org/lesson/635441/step/19?thread=solutions&unit=631831

from collections import Counter

def scrabble(symbols: str, word: str) -> bool:
    return Counter(symbols.lower()) >= Counter(word.lower())