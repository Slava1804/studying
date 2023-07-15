# https://stepik.org/lesson/594680/step/4?unit=589701

def recursive_sum(nested_lists):
    total = 0
    for i in nested_lists:
        if type(i) == int:
            total += i
        if type(i) == list:
            total += recursive_sum(i)
    return total