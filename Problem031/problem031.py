# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 31

# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
#                1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# How many different ways can £2 be made using any number of coins?


def make_change(coins,value):
    if value < 0:
        return 0
    if len(coins) == 1 or value == 0:
        return 1
    return make_change(coins[:-1],value) + make_change(coins,value-coins[-1])

print(make_change([1,2,5,10,20,50,100,200],200))