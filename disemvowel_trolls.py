# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string_):
    return ''.join(let for let in string_ if let.lower() not in 'aeiou')