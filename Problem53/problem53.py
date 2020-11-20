# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 53

# How many, not necessarily distinct, values of (n choose r) for 1<=n<=100, are greater than one-million?

    
from math import factorial as fact

def count_choose(max_n,comp):
    count = 0
    for n in range(1,max_n+1):
        for r in range(1,n+1):
            if fact(n) / (fact(r) * fact(n-r)) > comp:
                count += 1
    return count

print(count_choose(100,1000000))