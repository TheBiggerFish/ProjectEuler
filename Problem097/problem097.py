# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 97

# Find the last ten digits of 28433×2^7830457+1.


POWER = 7830457
MULTIPLE = 28433
ADDEND = 1
DIGITS = 10

val = 1
for _ in range(POWER):
    val *= 2
    val %= 10**DIGITS

print((val * MULTIPLE + ADDEND) % 10**DIGITS)