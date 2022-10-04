# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

def sort_array(list1):
    list1_ind = [i for i in range(len(list1)) if list1[i] % 2 == 0]
    list1_sym = [i for i in list1 if i % 2 == 0]
    list1_res = sorted([i for i in list1 if i % 2 != 0])
    for i in range(len(list1_ind)):
        list1_res.insert(list1_ind[i], list1_sym[i])
    return list1_res