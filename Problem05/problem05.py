# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


from multiset import Multiset
from math import prod

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

def prime_factors(number):
    if is_prime(number):
        return [number]
    for i in range(2,number):
        if number % i == 0 and is_prime(i):
            return [i] + prime_factors(int(number/i))

def smallest_multiple(upper):
    bag = Multiset([1])
    for i in range(2,upper+1):
        bag = bag.union(prime_factors(i))
    return prod(bag)

print(smallest_multiple(20))