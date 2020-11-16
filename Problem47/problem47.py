# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 47

# The first two consecutive numbers to have two distinct prime factors are:
#   14 = 2 × 7
#   15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
#   644 = 2² × 7 × 23
#   645 = 3 × 5 × 43
#   646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    for divisor in range(6, min(int(n**0.5) + 6,n-1), 6):
        if n % (divisor - 1) == 0 or n % (divisor + 1) == 0:
            return False
    return True

def prime_factors(number):
    if is_prime(number):
        return {number}
    for i in range(2,number):
        if number % i == 0:
            return prime_factors(i) | prime_factors(int(number/i))
    return set()

def consecutive_prime_factors(n,max_):
    consecutives = []
    for i in range(1,max_):
        if len(prime_factors(i)) == n:
            consecutives.append(i)
            # print(i,prime_factors(i))
        if len(consecutives) > 0 and consecutives[0] <= i - n:
            consecutives = consecutives[1:]
        if len(consecutives) == n:
            return consecutives
    return None

print(consecutive_prime_factors(4,10**6))