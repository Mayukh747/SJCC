



def dict_invert(d:dict):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    new_dict = dict()
    for k, v in d.items():
        if v in new_dict:
            new_dict[v].append(k)
            new_dict[v].sort()
        else:
            new_dict[v] = [k]
    return new_dict

if __name__ == '__main__':
    print(dict_invert({1:10, 2:20, 3:30}))
    print(dict_invert({1:10, 2:20, 3:30, 4:30}))
    print(dict_invert({4:True, 2:True, 0:True}))
