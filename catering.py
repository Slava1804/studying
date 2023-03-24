# https://stepik.org/lesson/623073/step/15?unit=618703

import json

districts = {}
company = {}
with open('food_services.json', encoding='utf-8') as file:
    data = json.load(file)

    for row in data:
        districts[row['District']] = districts.get(row['District'], 0) + 1
        if row['OperatingCompany']:
            company[row['OperatingCompany']] = company.get(row['OperatingCompany'], 0) + 1

    print(*max(districts.items(), key=lambda x: x[1]), sep=': ')
    print(*max(company.items(), key=lambda x: x[1]), sep=': ')