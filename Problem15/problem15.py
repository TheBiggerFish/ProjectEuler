# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 15

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?


from math import factorial as fact

w = 20
h = 20
print(int(fact(w+h)/(fact(w)*fact(h))))