# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 24

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


from itertools import permutations
perm = permutations([1,2,3,4,5,6,7,8,9,0])
print(sorted(list(perm))[999999])