# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


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

def sum_of_primes(max_):
    sum_ = 2
    for i in range(3,max_,2):
        if is_prime(i):
            sum_ += i
    return sum_

print(sum_of_primes(2000000))