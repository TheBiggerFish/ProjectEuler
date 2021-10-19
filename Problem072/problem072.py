# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 72

# How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?


from fishpy.primes import prime_factors, range_totient, sieve
from sympy.ntheory.factor_ import totient as phi


def num_proper_fractions(max_d,min_d=1):
    fracs = set()
    for d in range(max_d,max(min_d,max_d//2),-1):
        for n in range(1,d):
            div = n/d
            if div not in fracs:
                fracs.add(div)
    return len(fracs)

# print(num_proper_fractions(10000))
# run('num_proper_fractions(10000)')

def num_proper_fractions_2(max_):
    primes = sieve(max_)
    total = max_-1
    for i in range(2,max_):
        cur = 0
        if i in primes:
            total += (max_-i)-((max_-i)//i)
        else:
            if len(pf := prime_factors(i)) == 1:
                total += (max_-i)-((max_-i)//next(iter(pf)))
            else:
                total += range_totient(i,min_=i,max_=max_,factors=pf)
    return total

# print(num_proper_fractions_2(10000))
# run('num_proper_fractions_2(10000)')

def num_proper_fractions_3(max_):
    sum_ = 0
    for i in range(2,max_+1):
        sum_ += phi(i)
    return sum_

print(num_proper_fractions_3(1000000))
