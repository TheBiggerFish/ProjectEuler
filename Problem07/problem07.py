# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


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

def find_prime(which):
    i = 1
    cur = 0
    while cur < which:
        i += 1
        if is_prime(i):
            cur += 1
    return i


print(find_prime(10001))