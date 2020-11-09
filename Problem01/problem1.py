# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


max_value = 1000
multiplicands = [3,5]
sum_ = 0

for i in range(1,max_value):
    for multiplicand in multiplicands:
        if i % multiplicand == 0:
            sum_ += i
            break

print(sum_)