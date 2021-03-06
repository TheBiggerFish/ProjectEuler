# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 45

# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
# Triangle 	  	T_n=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
# Pentagonal 	  	P_n=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
# Hexagonal 	  	H_n=n(2n−1) 	  	1, 6, 15, 28, 45, ...
# It can be verified that T_285 = P_165 = H_143 = 40755.
# Find the next triangle number that is also pentagonal and hexagonal.


def gen_tri_nums(max_):
    tris = []
    for n in range(1,max_+1):
        tris.append(n*(n+1)//2)
    return tris

def gen_pen_nums(max_):
    pens = []
    for n in range(1,max_+1):
        pens.append(n*(3*n-1)//2)
    return pens

def gen_hex_nums(max_):
    hexes = []
    for n in range(1,max_+1):
        hexes.append(n*(2*n-1))
    return hexes

def find_intersect(max_):
    tris = set(gen_tri_nums(max_))
    pens = set(gen_pen_nums(max_))
    hexes = set(gen_hex_nums(max_))
    # print(tris.intersection(pens))
    return tris.intersection(pens).intersection(hexes)

print(find_intersect(1000000))
