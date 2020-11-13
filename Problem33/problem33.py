# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 33

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


from math import isclose

def to_list(number):
    return list([int(c) for c in str(number)])

def do_cancel(numer,denom):
    numer = to_list(numer)
    denom = to_list(denom)
    if numer[0] == denom[0]:
        if not denom[1] == 0:
            return numer[1]/denom[1]
    if numer[0] == denom[1]:
        return numer[1]/denom[0]
    if numer[1] == denom[0]:
        if not denom[1] == 0:
            return numer[0]/denom[1]
    if numer[1] == denom[1]:
        return numer[0]/denom[0]
    return -1

def cancel():
    product = float(1)
    for i in range(10,100):
        for j in range(i+1,100):
            if not i % 10 == j % 10 == 0:
                rv = do_cancel(i,j)
                if isclose(rv,i/j,rel_tol=1/10**5):
                    product *= i/j
    return round(product,5)



print(cancel())