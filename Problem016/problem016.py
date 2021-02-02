# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 16

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?


def sum_of_digits(number):
    return sum([int(c) for c in str(number)])

print(sum_of_digits(2**1000))