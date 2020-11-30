# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 73

# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?


def num_proper_fractions_range(max_d,min_d=1,min_ratio=0.0,max_ratio=1.0):
    found = 0
    frac = set()
    for d in range(min_d,max_d+1):
        n = int(min_ratio*d)+1
        while n/d < max_ratio:
            if n/d not in frac:
                frac.add(n/d)
                found += 1
            n += 1
    return found

print(num_proper_fractions_range(min_d=4,max_d=12000,min_ratio=1/3,max_ratio=1/2))