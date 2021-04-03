# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 99

# Determine which line number has the greatest numerical value.


from math import log10,pow

def estimate(base,exp):
    new_exp =  exp * log10(base)
    len = int(new_exp)
    lead = 10 ** (new_exp-len)
    return (len,lead)

values = []

with open('Problem099/base_exp.txt') as f:
    for line in f:
        nums = line.strip().split(',')
        base = int(nums[0])
        exp = int(nums[1])
        size,leading = estimate(base,exp)
        values.append((size,leading,base,exp))

print(sorted(values)[-1])
# print(len(str(999665**500894)))