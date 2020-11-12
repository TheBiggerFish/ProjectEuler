# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 28

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed by starting with the number 1 and moving to the right in a clockwise direction


def diagonal_sum(width):
    sum_ = 1
    i = 1
    step = 2
    while i < width**2:
        for _ in range(4):
            i += step
            sum_ += i
        step += 2
    return sum_

print(diagonal_sum(1001))