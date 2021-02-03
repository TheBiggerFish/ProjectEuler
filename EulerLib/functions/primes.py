from math import prod,gcd
from sympy.ntheory.factor_ import totient

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    for divisor in range(6, min(int(n**0.5) + 6,n-1), 6):
        if n % (divisor - 1) == 0 or n % (divisor + 1) == 0:
            return False
    return True

def factors(n):
    f = set()
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            f.add(i)
            f.add(n//i)
    return f
    
def prime_factors(n):
    f = set()
    if n % 2 == 0:
        f.add(2)
        while n % 2 == 0:
            n //= 2
    
    for i in range(3,int(n**0.5),2):
        if n % i == 0:
            f.add(i)
            while n % i == 0:
                n //= i
    if n > 1:
        f.add(n)
    return f

def sieve(max_):
    composite = set()
    for i in range(2,int(max_**0.5)+2):
        if i in composite:
            continue
        for j in range(i**2,max_,i):
            composite.add(j)
    return set(range(2,max_)).difference(composite)

def are_coprime(n1,n2):
    if n1 % n2 == 0 or n2 % n1 == 0:
        return False
    return gcd(n1,n2) == 0

# https://math.stackexchange.com/questions/1854197/calculate-the-number-of-integers-in-a-given-interval-that-are-coprime-to-a-given
def range_totient(n,max_,min_=2):
    full_range = int(max_-min_-((max_-min_)%n))
    rt = int(round(totient(n)/n * full_range,12))
    new_min = min_ + full_range + 1
    for i in range(new_min,max_+1):
        if are_coprime(i,n):
            rt += 1
    return rt