# https://stepik.org/lesson/518491/step/20?unit=510939

import csv


def condense_csv(filename, id_name):
    with open(filename, encoding='utf-8') as file:
        data = list(csv.reader(file, delimiter=','))
        result = {}

        for obj, char, value in data:
            if obj not in result:
                result[obj] = {id_name: obj}
            result[obj][char] = value

    with open('condensed.csv', 'w', encoding='utf-8', newline='') as file_res:
        writer = csv.DictWriter(file_res,
                                fieldnames=result[obj],
                                delimiter=',')
        writer.writeheader()
        writer.writerows(result.values())