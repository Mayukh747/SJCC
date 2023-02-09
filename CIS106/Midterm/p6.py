



def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    even = set()
    odd = set()

    for i in L:
        if i not in even and i not in odd:
            odd.add(i)
            continue
        if i in odd:
            odd.remove(i)
            even.add(i)
            continue
        if i in even:
            even.remove(i)
            odd.add(i)
    return None if not odd else max(odd)

''''
1. Frequency dict that maps int --> frequency
2. ^^ frequency dict that maps int --> odd/even bit
3. even set and odd set'''

if __name__ == '__main__':
    print(largest_odd_times([2,2,4,4]))
    print(largest_odd_times([3,9,5,3,5,3]))

