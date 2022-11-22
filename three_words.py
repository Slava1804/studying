def three_words(s):
    for c in range(1, len(s)):
        if set(s[0]) != set(s[c]):
            return 'NO'

    return 'YES'

st = input().split()
print(three_words(st))