def reverse_str(string:str):
    '''
    Simply reverses string
    '''
    # check the input
    if type(string) != str or not string:
        raise TypeError('Invalid type passed to function')

    # following lines should be commented out as needed.
    # use as cheetsheet
    # preference being method 2 of slicing  

    # # start method way 1: using reversed method()
    # return reversed(string)

    # # end method 1

    # # method 2: using list slicing
    # return string[::-1]
    # # end method 2

    # # method 3 using range() and list comprehension
    # # here we exploit the powers of range
    # # eg range(6, -1, -1)
    # # gives an iterable of [6,5,4,3,2,1]
    # _range = range(start=len(string)-1, stop=-1, step=-1)
    # return ''.join([i for i in _range])
    # # end method 3

    # # start method 4 using loops 
    # rev_list = [ ]
    # last_index = len(string) - 1
    # while last_index > 0:
    #     rev_list.append(string[last_index])
    #     last_index -= 1
    
    # return ''.join(rev_list)
    # # end method 2

    pass


def merge_2_sorted_arrays(array_1:list, array_2:list):
    return sorted((array_1 + array_2))


def find_first_recurring(ar):
    # TODO this is common google question
    # given array find the first recurring element
    # eg [2,3,4,5,6,2,6]
    # in the example the answer will be 2

    viewed = {}
    # O(n)
    for el in ar:
        if viewed.get(el):
            return el
        else:
            viewed[el] = 1
    return None


print(find_first_recurring([2,4,5,6,7,5,6]))