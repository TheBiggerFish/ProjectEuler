# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 14

# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.


stored = {1:1}

def sequence(value):
    steps = 1
    while value > 1:
        if value in stored:
            steps += stored[value]
            break
        if value % 2 == 0:
            value /= 2
        else:
            value = value * 3 + 1
        steps += 1
    return steps

def longest_collatz(max_start):
    max_ = 1
    for i in range(max_start):
        stored[i] = sequence(i)
        if stored[i] > stored[max_]:
            max_ = i
    return max_
        
print(longest_collatz(1000000))