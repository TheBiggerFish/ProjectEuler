# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 60

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. 
# For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.


from itertools import combinations as combs
from math import log10 as log

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    for divisor in range(6, min(int(n**0.5) + 6,n-1), 6):
        if n % (divisor - 1) == 0 or n % (divisor + 1) == 0:
            return False
    return True

def evaluate(a,b):
    len_a = int(log(a))+1
    len_b = int(log(b))+1
    return is_prime(int(a*(10**len_b)+b)) and is_prime(int(b*(10**len_a)+a))

def sieve(max_):
    composite = set()
    for i in range(2,max_):
        if i in composite:
            continue
        for j in range(i**2,max_,i):
            composite.add(j)
    return sorted(set(range(2,max_)).difference(composite))

def prime_pairs(max_):
    primes = sieve(max_+1)
    for i in primes:
        for j in primes:
            if i >= j or not evaluate(i,j):
                continue
            for k in primes:
                if j >= k:
                    continue
                found = False
                for pair in [(i,k),(j,k)]:
                    if not evaluate(*pair):
                        found = True
                        break
                if found:
                    continue
                for l in primes:
                    if k >= l:
                        continue
                    found = False
                    for pair in [(i,l),(j,l),(k,l)]:
                        if not evaluate(*pair):
                            found = True
                            break
                    if found:
                        continue
                    for m in primes:
                        if l >= m:
                            continue
                        found = False
                        for pair in [(i,m),(j,m),(k,m),(l,m)]:
                            if not evaluate(*pair):
                                found = True
                                break
                        if found:
                            continue
                        return sum((i,j,k,l,m))

    return -1

print(prime_pairs(10000))