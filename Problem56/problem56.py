# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 55

# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?


def sum_of_digits(number):
    return sum([int(c) for c in str(number)])

print(max([sum_of_digits(a**b) for a in range(100) for b in range(100)]))