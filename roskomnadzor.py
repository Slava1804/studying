# https://stepik.org/lesson/415554/step/11?unit=405083

s = input() + ' запретил букву'
list_sym =  ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
i = 0
while len(s) != 0:
    if list_sym[i] not in s:
        i += 1
    else:
        print(s.lstrip(), list_sym[i])
        s = s.replace(list_sym[i], '').strip().replace('  ', ' ')
        i += 1