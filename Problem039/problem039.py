# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 39

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120. {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?


def gen_right_triangles(p):
    rights = set()
    for L1 in range(1,p//3+1):
        for L2 in range(L1,p//2+1):
            H = p - L1 - L2
            if L1**2 + L2**2 == H**2:
                rights.add((L1,L2,H))
    return rights

def num_right_triangles(max_p):
    max_len = 1
    max_val = 12
    for p in range(12,max_p+1):
        rv = len(gen_right_triangles(p))
        if rv > max_len:
            max_val = p
            max_len = rv
    return max_val

print(num_right_triangles(1000))