# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 25

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


def fibonacci_digits(digits):
    index = 0
    cur = 0
    prev = 1
    while True:
        if cur >= 10**(digits-1):
            return index
        temp = cur + prev
        prev = cur
        cur = temp
        index += 1

print(fibonacci_digits(1000))