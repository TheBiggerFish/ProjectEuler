# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 46

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#   9 = 7 + 2×1^2
#   15 = 7 + 2×2^2
#   21 = 3 + 2×3^2
#   25 = 7 + 2×3^2
#   27 = 19 + 2×2^2
#   33 = 31 + 2×1^2
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?


from math import isclose

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    for divisor in range(6, min(int(n**0.5) + 7,n-1), 6):
        if n % (divisor - 1) == 0 or n % (divisor + 1) == 0:
            return False
    return True

def gen_primes(max_):
    lst = [2,3]
    for i in range(6, max_, 6):
        if is_prime(i-1):
            lst.append(i-1)
        if is_prime(i+1):
            lst.append(i+1) 
    return lst

def is_goldbach(number,primes):
    for prime in primes:
        if number < prime:
            break
        if (((number - prime)/2)**0.5).is_integer():
            return True
    return False

def find_non_goldbach(max_):
    primes = gen_primes(max_)
    for i in range(9,max_,2):
        if not is_prime(i):
            if not is_goldbach(i,primes):
                return i
    return 'none found'

print(find_non_goldbach(10000))