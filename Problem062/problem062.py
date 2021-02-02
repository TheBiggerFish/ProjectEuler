# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 62

# The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). 
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
# Find the smallest cube for which exactly five permutations of its digits are cube.


def gen_cubes(max_):
    cubes = {}
    for i in range(1,max_+1):
        key = ''.join(sorted(str(i**3)))
        cubes[key] = cubes[key] + [i**3] if key in cubes else [i**3]
    return cubes

def cube_perms(max_,num_cubes):
    cubes = gen_cubes(max_)
    min_ = 10**100
    for cube in sorted(cubes.keys()):
        if len(cubes[cube]) >= num_cubes:
            if min_ > min(cubes[cube]):
                min_ = min(cubes[cube])
    return min_

print(cube_perms(10000,5))