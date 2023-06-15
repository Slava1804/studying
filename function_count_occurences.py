# https://stepik.org/lesson/590120/step/16?thread=solutions&unit=585064

from collections import Counter

def count_occurences(word: str, words: str) -> int:
    return Counter(words.lower().split())[word.lower()]