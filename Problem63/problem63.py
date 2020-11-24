# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 63

# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?


from math import log10 as log

def powerful_digit_counts(max_b,max_p):
    count = 0
    for b in range(1,max_b):
        for p in range(1,max_p):
            if len(str(b**p)) == p:
                count += 1
    return count

print(powerful_digit_counts(100,100))