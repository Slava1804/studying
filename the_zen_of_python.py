# https://stepik.org/lesson/590120/step/19?thread=solutions&unit=585064

from collections import Counter

with open('pythonzen.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    letters = Counter([c.lower() for c in text if c.isalpha()])
    
    for letter, count in sorted(letters.items()):
        print(f'{letter}: {count}') 