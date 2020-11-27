def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    for divisor in range(6, min(int(n**0.5) + 6,n-1), 6):
        if n % (divisor - 1) == 0 or n % (divisor + 1) == 0:
            return False
    return True

def prime_factors(n,primes=None):
    if (primes is None and is_prime(n)) or (primes is not None and n in primes):
        return {n}
    for i in range(2,n):
        if n % i == 0:
            return prime_factors(i) | prime_factors(int(n/i))
    return set()

def sieve(max_):
    composite = set()
    for i in range(2,int(max_**0.5)+2):
        if i in composite:
            continue
        for j in range(i**2,max_,i):
            composite.add(j)
    return set(range(2,max_)).difference(composite)