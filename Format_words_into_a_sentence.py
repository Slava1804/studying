# https://www.codewars.com/kata/51689e27fe9a00b126000004

def format_words(words):
    if not words:
        return ''
    elif len(words) == 1:
        return words[0]
    else:
        words = [w for w in words if w]

        if len(words) == 1:
            return words[0]
        else:
            return f"{', '.join(words[:-1])} and {words[-1]}"