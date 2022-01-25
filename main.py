# incase I want to use a more familiar language
def search_for_common(ar_1, ar_2):
    '''
    To confirm if there are common elements
    '''
    # there goes readability
    common_elements = set(ar_1).intersection(ar_2)

    return len(common_elements) > 0


response = search_for_common([1,3,4,5,6], [2,3,4,5])
print(response)