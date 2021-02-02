# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 30

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


def sum_of_powers(number,power):
    return sum([int(c)**power for c in str(number)])

def sum_of_sums(max_num,power):
    sum_ = 0
    for i in range(2,max_num):
        rv = sum_of_powers(i,power)
        if i == rv:
            sum_ += i
    return sum_

print(sum_of_sums(250000,5))