# https://stepik.org/lesson/634670/step/23?thread=solutions&unit=630932

from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

ingriedents = ChainMap(bread, meat, sauce, vegetables, toppings)
order = Counter(input().split(','))
result = f'ИТОГ: {sum([v*ingriedents[k] for k, v in order.items()])}р'
symbol, count_max = len(max(order, key=len)), len(str(max(order.values())))

for vegatable, count in sorted(order.items()):
    print(f'{vegatable}{(symbol-len(vegatable))*" "} x {count}')
print(f'{"-"*(symbol+3+count_max if symbol+3+count_max > len(result) else len(result))}\n{result}') 