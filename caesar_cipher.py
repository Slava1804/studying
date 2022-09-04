alp_en = 'abcdefghijklmnopqrstuvwxyz' * 2
alp_en_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2
alp_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя' * 2
alp_ru_big = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' * 2
way_sh = input('Выберите направление - шифрование или дешифрование: ')
language_sh = input('Выберите нужный язык: ')
words_sh = input('Введите предложение для процесса: ')
step = int(input('Назовите шаг сдвига: '))
res = ''
if way_sh == 'шифрование':
    if language_sh == 'en':
        for i in range(len(words_sh)):
            if words_sh[i] in ' !?,.-':
                res += words_sh[i]
            elif words_sh[i].isupper():
                a = alp_en_big.find(words_sh[i]) + step
                res += alp_en_big[a]
            else:
                a = alp_en.find(words_sh[i]) + step
                res += alp_en[a]
    else:
        for i in range(len(words_sh)):
            if words_sh[i] in ' !?,.-':
                res += words_sh[i]
            elif words_sh[i].isupper():
                a = alp_ru_big.find(words_sh[i]) + step
                res += alp_ru_big[a]
            else:
                a = alp_ru.find(words_sh[i]) + step
                res += alp_ru[a]
else:
    if language_sh == 'en':
        for i in range(len(words_sh)):
            if words_sh[i] in ' !?,.-':
                res += words_sh[i]
            elif words_sh[i].isupper():
                a = alp_en_big.find(words_sh[i]) - step
                res += alp_en_big[a]
            else:
                a = alp_en.find(words_sh[i]) - step
                res += alp_en[a]
    else:
        for i in range(len(words_sh)):
            if words_sh[i] in ' !?,.-':
                res += words_sh[i]
            elif words_sh[i].isupper():
                a = alp_ru_big.find(words_sh[i]) - step
                res += alp_ru_big[a]
            else:
                a = alp_ru.find(words_sh[i]) - step
                res += alp_ru[a]
print(res)