# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 43

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#    d2d3d4=406 is divisible by 2
#    d3d4d5=063 is divisible by 3
#    d4d5d6=635 is divisible by 5
#    d5d6d7=357 is divisible by 7
#    d6d7d8=572 is divisible by 11
#    d7d8d9=728 is divisible by 13
#    d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.


from itertools import permutations as perm

def list_to_num(lst):
    num = 0
    for i in range(len(lst),0,-1):
        num += 10**(i-1) * lst[-i]
    return num

def matches_pattern(num):
    if not num[3] % 2 == 0:
        return False
    if not list_to_num(num[2:5]) % 3 == 0:
        return False
    if not num[5] % 5 == 0:
        return False
    if not list_to_num(num[4:7]) % 7 == 0:
        return False
    if not list_to_num(num[5:8]) % 11 == 0:
        return False
    if not list_to_num(num[6:9]) % 13 == 0:
        return False
    if not list_to_num(num[7:10]) % 17 == 0:
        return False
    return True

def find_sum_pans():
    sum_ = 0
    for lst in [lst for lst in perm(range(0,10))]:
        if matches_pattern(lst):
            sum_ += list_to_num(lst)
    return sum_

print(find_sum_pans())