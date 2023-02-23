# https://www.codewars.com/kata/52223df9e8f98c7aa7000062

def rot13(message):
    letters = 'abcdefghijklmnopqrstuvwxyz'*2
    result = ''
    
    for sym in message:
        if sym.isalpha():
            ind = letters.index(sym.lower())
            if sym.isupper():
                result += letters[13+ind].upper()
            else:
                result += letters[13+ind]
        else:
            result += sym
    return result