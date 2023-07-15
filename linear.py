# https://stepik.org/lesson/594680/step/5?unit=589701

def linear(nested_lists):
    new_list=[]
    for i in nested_lists:
        if isinstance(i, int):
            new_list.append(i)
        else:
            new_list.extend(linear(i))
    return new_list