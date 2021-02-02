# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


import math

def triplet(sum_):
    for i in range(1,int(sum_/3)):
        for j in range(i,int(sum_/2)):
            for k in range(sum_-(i+j),sum_):
                if i*i + j*j == k*k and i+j+k == sum_:
                    return (i,j,k)


print(math.prod(triplet(1000)))