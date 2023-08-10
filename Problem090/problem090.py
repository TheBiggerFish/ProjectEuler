# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 90

# How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?


from itertools import combinations

dice = list(combinations(range(0,10), 6))
for die in dice:
    print(die)