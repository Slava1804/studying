# https://www.codewars.com/kata/5839edaa6754d6fec10000a2 

def find_sym(list_sym):
    if list_sym[0].islower():
        alp = [chr(i).lower() for i in range(65, 91)]
    else:
        alp = [chr(i).upper() for i in range(65, 91)]
    s = alp[alp.index(list_sym[0]):alp.index(list_sym[-1])+1]
    for i in s:
        if i not in list_sym:
            return i