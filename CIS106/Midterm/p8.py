



def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def func(x):
        sum = 0
        pow = 0
        for coefficient in reversed(L):
            sum += (x**pow) * coefficient
            pow += 1
        return sum
    return func

if __name__ == '__main__':
    l = [1,2,3,4]
    f = general_poly(l)
    print(f(10))
