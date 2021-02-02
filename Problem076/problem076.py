# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 76

# How many different ways can one hundred be written as a sum of at least two positive integers?
# Based on my solution to problem 31


def count_sums(value,sub):
    if value < 0:
        return 0
    if value == 0 or sub == 1:
        return 1
    return count_sums(value,sub-1) + count_sums(value-sub,sub)

print(count_sums(100,99))