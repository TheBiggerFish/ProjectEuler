# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 35

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# How many circular primes are there below one million?


from math import floor,log10

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(n**0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def gen_rotations(number):
    digits = floor(log10(number))+1
    rotations = set()
    for _ in range(digits):
        rotations.add(number)
        last = number%10
        number //= 10
        number += last * 10**(digits-1)
    return rotations

def all_prime(numbers):
    for num in numbers:
        if not is_prime(num):
            return False
    return True

def circular_primes(max_):
    circ = {2}
    for i in range(3,max_):
        if len([x for x in str(i) if x in '02468']) > 0:
            continue
        rots = gen_rotations(i)
        if all_prime(rots):
            circ = circ | rots
    return circ

print(len(circular_primes(1000000)))