

def is_triangular(k) -> bool:
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    t_num = 1
    i = 2
    while t_num < k:
        t_num += i
        i += 1
    return t_num == k

def print_n_triangular_nums(n):
    total = 0
    for i in range(1, n+1):
        total += i
        print(total)


if __name__ == '__main__':
    #print_n_triangular_nums(3)
    for i in range(20):
        print(i, is_triangular(i))
