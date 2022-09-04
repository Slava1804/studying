from random import*
t = 0
num = randint(1, 100)
print('!!Добро пожаловать в числовую угадайку!!')

def is_valid(num_error): 
    if num_error.isdigit():
        if 0 < int(num_error) < 101:
            return True
    else:
        return False

while True:
    print()
    num_usser = input('Введите число от одного до ста: ')
    if is_valid(num_usser):
        t += 1
        num_usser = int(num_usser)
        if num_usser == num:
            print('Вы угадали, поздравляем!')
            print()
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            print('Данные о сессии: ', 'Количество попыток: ' + str(t), sep='\n')
            break
        elif num_usser < num:
            print()
            print('Слишком мало, попробуйте еще раз')
        else:
            print()
            print('Слишком много, попробуйте еще раз')
    else:
        print()
        print('А может быть все-таки введем целое число от 1 до 100?')