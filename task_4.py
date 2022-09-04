def find_all(target, symboll):
    m = [i for i in range(len(target)) if target[i] == symboll]
    return m

s, s1 = input(), input()
print(find_all(s, s1))