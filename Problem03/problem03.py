# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


# Simple optimized is_prime function taken from https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
def is_prime(number):
    # Corner cases 
    if (number <= 1) : 
        return False
    if (number <= 3) : 
        return True
    if (number % 2 == 0 or number % 3 == 0) : 
        return False
    i = 5
    while(i * i <= number) : 
        if (number % i == 0 or number % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

# Recursive function that returns a list of prime factors
def prime_factors(number):
    if is_prime(number):
        return [number]
    for i in range(2,number):
        if number % i == 0:
            return prime_factors(i) + prime_factors(int(number/i))

print(prime_factors(600851475143)[-1])