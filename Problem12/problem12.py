# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 12

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#     1: 1
#     3: 1,3
#     6: 1,2,3,6
#    10: 1,2,5,10
#    15: 1,3,5,15
#    21: 1,3,7,21
#    28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?


def factors(number):
    f = {1,number}
    sqr = int(number**0.5) + 1
    for divisor in range(2, sqr):
        if number % divisor == 0:
            f.add(divisor)
            f.add(int(number/divisor))
    return sorted(f)

def triangle(divisors):
    value = 1
    i = 2
    while True:
        if len(factors(value)) > divisors:
            return value
        value += i
        i += 1

print(triangle(500))