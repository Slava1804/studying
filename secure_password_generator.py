from random import*

digits = '0123456789'
lowercase_letters = 'qwertyuiopasdfghjklzxcvbnm'
uppercase_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
punctuation = '!#$%&*+-=?@^_'
chars = ''
num_iteration = int(input('Назовите количество паролей для генерации: '))

def generate_password(length, char):
    password = ''
    for _ in range(length):
        password += choice(char)
    return password

for _ in range(num_iteration):
    chars = ''
    len_password = int(input('Назовите длину пароля: '))
    question_digit = input('Должен ли пароль включать цифры? ')
    if question_digit.lower() == 'да':
        chars += digits 
    upper_sym = input('Включать прописные буквы? ')
    if upper_sym.lower() == 'да':
        chars += uppercase_letters
    lower_sym = input('Включать строчные буквы? ')
    if lower_sym.lower() == 'да':
        chars += lowercase_letters
    sym = input('Включать символы? ')
    if sym.lower() == 'да':
        chars += punctuation
    print(generate_password(len_password, chars))