def duplicate_count(text):
    text = text.lower()
    t = 0
    for i in text:
        if text.count(i) > 1:
            t += 1
            text = text.replace(i, ' ')
    return t

s = input()
print(duplicate_count(s))
     