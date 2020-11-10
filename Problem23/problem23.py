# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 23

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def factor(number):
    f = {1}
    sqr = int(number**0.5) + 1
    for divisor in range(2, sqr):
        if number % divisor == 0:
            f.add(divisor)
            f.add(int(number/divisor))
    return sorted(f)

def is_abundant(number):
    return sum(factor(number)) > number

def not_sum_of_abundants():
    not_sums = []
    abundants = set()
    for i in range(1,28123):
        if is_abundant(i):
            abundants.add(i)
    for i in range(1,28124):
        found = False
        for abundant in abundants:
            if i-abundant in abundants:
                found = True
                break
        if not found:
            not_sums.append(i)
    return not_sums

print(sum(not_sum_of_abundants()))