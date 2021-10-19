# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 71

# By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.


from fishpy.fraction import Fraction


def gen_proper_fractions(max_d,min_d=1,min_ratio=0.0,max_ratio=1.0):
    fracs = set()
    for d in range(min_d,max_d+1):
        n = int(min_ratio*d)+1
        while min_ratio < n/d < max_ratio:
            fracs.add(Fraction(n,d).reduce())
            n += 1
    return fracs

print(max(gen_proper_fractions(max_d=10**6,min_ratio=299999/700000,max_ratio=3/7)).n)
