# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 32

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


def is_pan(str_):
    if len(str_) != 9:
        return False
    for i in range(1,10):
        if str(i) not in str_:
            return False
    return True

def get_pans():
    all_pans = set()
    for i in range(0,10):
        for j in range(1000,10000):
            if is_pan(str(i)+str(j)+str(i*j)):
                all_pans.add(i*j)
    for i in range(10,100):
        for j in range(100,1000):
            if i * j >= 10000:
                break
            if is_pan(str(i)+str(j)+str(i*j)):
                all_pans.add(i*j)
    return all_pans

print(sum(get_pans()))