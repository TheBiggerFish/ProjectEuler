# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 69

# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
# https://en.wikipedia.org/wiki/Euler%27s_totient_function


from EulerLib.functions.primes import prime_factors,sieve
from math import prod

def totient(n,primes=None):
    factors = prime_factors(n,primes)
    return round(prod([1-(1/factor) for factor in factors]) * n)

def least_totient(max_):
    primes = sieve(max_)
    best_n = 0
    best_tot = 1
    for n in range(2,max_):
        if n in primes:
            continue
        tot = totient(n,primes)
        if n / tot > best_n / best_tot:
            best_n = n
            best_tot = tot
    return best_n

print(least_totient(10**6))