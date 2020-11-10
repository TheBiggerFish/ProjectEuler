# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 20

# Find the sum of the digits in the number 100!


from math import factorial
def sum_of_digits(number):
    return sum([int(c) for c in str(number)])

print(sum_of_digits(factorial(100)))