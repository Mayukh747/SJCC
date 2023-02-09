

# def print_without_vowels(s):
#     '''
#     s: the string to convert
#     Finds a version of s without vowels and whose characters appear in the
#     same order they appear in s. Prints this version of s.
#     Does not return anything
#     '''
#
    vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    ans = ""

    for c in s:
        if c not in vowel_set:
            ans += c
    print(ans)

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    letter = []
    for i in s:
        if i not in vowels:
            #letter.append(i)
            print(i)
    # print(str(letter))


if __name__ == '__main__':
    #print_n_triangular_nums(3)
    print_without_vowels("This is great!")
