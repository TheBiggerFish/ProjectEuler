# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 36 

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.


def is_palindrome(string):
    return string == string[::-1]

def double_palindrome(number):
    return is_palindrome(str(number)) and is_palindrome("{0:b}".format(number))

def sum_palindrome(max_):
    sum_ = 0
    for i in range(max_):
        if double_palindrome(i):
            sum_ += i
    return sum_

print(sum_palindrome(1000000))