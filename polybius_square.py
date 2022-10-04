hard_dictionary = {
    "А": "11",
    "Б": "12",
    "В": "13",
    "Г": "14",
    "Д": "15",
    "Е": "16",
    "Ё": "21",
    "Ж": "22",
    "З": "23",
    "И": "24",
    "Й": "25",
    "К": "26",
    "Л": "31",
    "М": "32",
    "Н": "33",
    "О": "34",
    "П": "35",
    "Р": "36",
    "С": "41",
    "Т": "42",
    "У": "43",
    "Ф": "44",
    "Х": "45",
    "Ц": "46",
    "Ч": "51",
    "Ш": "52",
    "Щ": "53",
    "Ъ": "54",
    "Ы": "55",
    "Ь": "56",
    "Э": "61",
    "Ю": "62",
    "Я": "63"
}

res = ' '.join([
    hard_dictionary[i]
    for i in input('Введите слово для зашифровки и расшифровки: ').upper()
])

print()
print(res, '- зашифрованное слово')
print()

n_file = open('new_file.txt', 'w')
n_file.write(res)
n_file.close

with open('new_file.txt', 'r') as n_file:
    read_file = n_file.read()

res_list = read_file.split()
s = ''

for i in res_list:
    for key, values in hard_dictionary.items():
        if i == values:
            s += key
            break

print(s, '- расшифровка')