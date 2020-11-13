# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 37

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.



from math import floor,log10
def all_truncations(number):
    digits = floor(log10(number))+1
    string = str(number)
    truncs = {number} | set([int(''.join([x for x in string[:i]])) for i in range(1,digits)])
    return truncs | set([int(''.join([x for x in string[i:]])) for i in range(1,digits)])

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for divisor in range(3, int(n**0.5) + 1, 2):
        if n % divisor == 0:
            return False
    return True

def prime_truncatable(number):
    for num in all_truncations(number):
        if not is_prime(num):
            return False
    return True

def find_prime_truncatables(max_):
    truncs = set()
    for i in range(23,max_,2):
        if prime_truncatable(i):
            truncs.add(i)
    return truncs

print(sum(find_prime_truncatables(1000000)))