# https://stepik.org/lesson/635441/step/21?unit=631831

from collections import Counter
import csv, json

with open('prices.json', encoding='utf-8') as f:
    data = json.load(f)
    
result = Counter()

for file_name in ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']:
    with open(file_name, encoding='utf-8') as file:
        _, *rows = csv.reader(file)

        for vegetable, *prices in rows:
            result[vegetable] += sum(map(int, prices))*data[vegetable]

print(result.total())