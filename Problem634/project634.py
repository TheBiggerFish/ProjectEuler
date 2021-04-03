# Written by Cameron Haddock and Daniel Millson
# Submitted as a solution to Project Euler's Problem 634

# Define F(n) to be the number of integers x <= n that can be written in the form x = a^2 * b^3, where a and b are integers not necessarily different and both greater than 1.
# Find F(9 x 10^18).

from EulerLib.debug import profile,timer
import numpy as np

n = 2*10**4
highest = int(n**(1/5))+1
num_threads = 8
precision = 8

s = set()
# sets = []


def old_search(high):
    # a**2 * b**3
    counts = {}
    
    for a in range(2, high):   # n//8+1
        counts[f'{a}^2'] = 0
        p = a**2
        if p > n:
            break
        for b in range(a, int((n/p)**(1/3))+1):      # n//4+1
            q = b**3
            x = p * q
            if x > n:
                break
            if x in s:
                continue
            counts[f'{a}^2'] += 1
            s.add(x)
    # a**3 * b**2
    for a in range(2, high):        # n//4+1
        counts[f'{a}^3'] = 0
        p = a**3
        if p > n:
            break
        for b in range(a, int((n/p)**(1/2))+1): # n//8+1
            q = b**2
            x = p * q
            if x > n:
                break
            if x in s:
                continue
            counts[f'{a}^3'] += 1
            s.add(x)
    for c in sorted(counts.keys()):
        print(c,counts[c])


def search(high):
    debug = set()
    found = set()
    count = 0
    # a**2 * b**3
    
    for a in range(2,high):   # n//8+1
        p = a**2
        q = a**3
        r = a**5
        if p <= n / 8:
            # b = int((n/p)**(1/3))-a+1
            # print(f'{a}^2',b)
            # count += b
            for b in range(a,int((n/p)**(1/3))+1):
                string = f'{a}^2*{b}^3'
                if a**2*b**3 not in found:
                    found.add(a**2*b**3)
                else:
                    print('WHY')
                print(string,a**2*b**3)
                count += 1
        if q <= n / 4 and r <= n:
            # b = int((n/q)**(1/2))-a
            # print(f'{a}^3',b)
            # count += b
            for b in range(a+1,int((n/q)**(1/2))+1):
                string = f'{b}^2*{a}^3'
                if b**2*a**3 not in found:
                    found.add(b**2*a**3)
                else:
                    print('WHY')
                print(string,b**2*a**3)
                count += 1
        else:
            break
    return count

old_search(highest)
print()
print(search(highest))