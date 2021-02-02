# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 34

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.


from math import factorial
def factorial_sum(number):
    return sum([factorial(int(c)) for c in str(number)])

def find_factorial_sums(max_):
    sum_ = 0
    for i in range(3,max_+1):
        if factorial_sum(i) == i:
            sum_ += i
    return sum_

print(find_factorial_sums(100000))