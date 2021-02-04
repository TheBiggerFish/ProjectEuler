# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 85

from math import gcd

# A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.
# However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.
# It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.
# Find the least value of M such that the number of solutions first exceeds one million.


def gen_perfect_squares(M):
    bound = int(100*M)
    return {i**2 for i in range(1,bound+1)}

def num_new_solutions(old_M,M,perfect_squares):
    count = 0

    for w in range(1,old_M+1):
        for l in range(w,old_M+1):
            sq = (l+w)**2
            for h in range(old_M+1,M+1):
                if (sq + h**2) in perfect_squares:
                    count += 1
        if w%10 == 0:
            print(w/old_M)
        
    for w in range(1,old_M+1):
        for l in range(old_M+1,M+1):
            sq = (l+w)**2
            for h in range(l,M+1):
                if (sq + h**2) in perfect_squares:
                    count += 1
        if w%10 == 0:
            print(w/old_M)

    for w in range(old_M+1,M+1):
        for l in range(w,M+1):
            sq = (l+w)**2
            for h in range(l,M+1):
                if (sq + h**2) in perfect_squares:
                    count += 1
        if w%10 == 0:
            print((w-old_M)/(M-old_M))

    return count

# def num_integer_solutions(M,perfect_squares):
#     count = 0
#     for w in range(1,M+1):
#         for l in range(w,M+1):
#             sq = (l+w)**2
#             for h in range(l,M+1):
#                 if (sq + h**2) in perfect_squares:
#                     count += 1
#         if w%10 == 0:
#             print(w/M)
#     return count

def zero_in(target,precision=500):
    M = 5
    old_M = 1
    count = 0
    while True:
        count += num_new_solutions(old_M,M,gen_perfect_squares(M))
        print(M,count)
        diff = abs(target - count)
        if diff < precision:
            return M if count > target else M+1
        old_M = M
        if diff < 10*precision:
            M += 1
        else:
            M = int(M * (target/count)**0.4)

print(zero_in(1000000))