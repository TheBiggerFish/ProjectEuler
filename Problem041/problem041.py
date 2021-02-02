# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 41

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?


from itertools import permutations as perm

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    for divisor in range(6, int(n**0.5) + 1, 6):
        if n % (divisor - 1) == 0 or n % (divisor + 1) == 0:
            return False
    return True

def list_to_num(lst):
    num = 0
    for i in range(len(lst),0,-1):
        num += 10**(i-1) * lst[-i]
    return num

def find_prime_pan(n_digits):
    for num in reversed([list_to_num(lst) for lst in perm(range(1,n_digits+1))]):
        if num % 10 in [0,2,4,5,6,8]:
            continue
        if is_prime(num):
            return num
    return -1

def find_longest_prime_pan(max_digits):
    for i in range(max_digits,1,-1):
        rv = find_prime_pan(i)
        if rv != -1:
            return rv
    return -1

print(find_longest_prime_pan(9))