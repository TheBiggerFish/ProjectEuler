# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(number):
    return str(number) == str(number)[::-1]

def largest_palindrome(digits):
    max_ = 0
    for i in range(1,10**digits):
        for j in range(1,10**digits):
            if i*j > max_ and is_palindrome(i*j):
                max_ = i*j
    return max_

print(largest_palindrome(3))