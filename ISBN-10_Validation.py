# https://www.codewars.com/kata/51fc12de24a9d8cb0e000001

def valid_ISBN10(isbn): 
    if len(isbn) == 10 and isbn[:-1].isdigit():
        if isbn[-1].isalpha() and isbn[-1] != 'X':
            return False
        res = 0

        for i in range(10):
            if isbn[i].isdigit():
                res += int(isbn[i]) * (i+1)
            else:
                res += 10 * (i+1)

        return  res % 11 == 0

    return False