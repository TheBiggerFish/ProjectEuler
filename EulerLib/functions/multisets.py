from multiset import Multiset
from primes import is_prime

def multiset_prime_factors(n,primes=None):
    if (primes is None and is_prime(n)) or (primes is not None and n in primes):
        return Multiset([n])
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return multiset_prime_factors(i) + multiset_prime_factors(int(n/i))
    return Multiset([])