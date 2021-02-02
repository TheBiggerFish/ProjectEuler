# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 70

# Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.


from EulerLib.functions.primes import sieve,prime_factors
from math import prod

def is_permutation(a,b):
    return sorted(str(a)) == sorted(str(b))

found = {}
def totient(n,primes=None):
    if n % 4 == 0 and n > 4:
        tot = 2*found[n//2]
    elif n % 2 == 0 and n > 4:
        tot = found[n//2]
    else:
        factors = prime_factors(n,primes)
        tot = round(prod([1-(1/factor) for factor in factors]) * n)
    found[n] = tot
    return tot

def least_totient_perm(max_):
    primes = sieve(max_)
    best_n = max_+1
    best_tot = 1
    for n in range(2,max_):
        if n % 500000 == 0:
            print(n)
        if n in primes:
            found[n] = n-1
            continue
        tot = totient(n,primes)
        if n / tot < best_n / best_tot:
            if is_permutation(n,tot):
                best_n = n
                best_tot = tot
    return best_n

print(least_totient_perm(10**7))