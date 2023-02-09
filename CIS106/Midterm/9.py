def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    dict1 = create_freq_dict(L1)
    dict2 = create_freq_dict(L2)
    if dict1 == dict2:
        result = max(dict1, key=dict1.get)

        return result, dict1[result], type(result) if result!=None else \
            None, None, None
    else:
        return False

def create_freq_dict(L) -> dict:
    d = dict()
    for element in L:
        if element in d:
            d[element] += 1
        else:
            d[element] = 1
    return d


if __name__ == '__main__':
    # L1 = ['a', 'a', 'b']
    # L2 = ['a', 'b']
    L1 = [1, 'b', 1, 'c', 'c', 1]
    L2 = ['c', 1, 'b', 1, 1, 'c']
    print(is_list_permutation(L1,L2))
