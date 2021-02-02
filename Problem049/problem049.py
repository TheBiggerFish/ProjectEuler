# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 49

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
#   (1) Each of the three terms are prime
#   (2) Each of the 4-digit numbers are permutations of one another
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?


from itertools import permutations as perm

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    for divisor in range(6, min(int(n**0.5) + 6,n-1), 6):
        if n % (divisor - 1) == 0 or n % (divisor + 1) == 0:
            return False
    return True
    
def num_to_list(num):
    lst = []
    size = len(str(num))
    for i in range(size):
        lst.append(num // (10**(size-i-1)) % 10)
    return lst

def list_to_num(lst):
    num = 0
    for i in range(len(lst),0,-1):
        num += 10**(i-1) * lst[-i]
    return num

def find_seq():
    checked = set()
    for i in range(10**3,10**4):
        if i in checked:
            continue

        perms = [list_to_num(lst) for lst in perm(num_to_list(i))]
        primes = sorted(set([num for num in perms if num >= 1000 and is_prime(num)]))

        if len(primes) >= 3:
            for x in range(len(primes)-2):
                for y in range(x+1,len(primes)-1):
                    for z in range(y+1,len(primes)):
                        if primes[z] - primes[y] == primes[y] - primes[x]:
                            return(primes[x],primes[y],primes[z])
        checked = checked.union(set(perms))
    return 'not found'

print(find_seq())