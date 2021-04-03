# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 86

from math import gcd

# A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.
# However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.
# It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.
# Find the least value of M such that the number of solutions first exceeds one million.


# def gen_perfect_squares(M):
#     bound = int(2**0.5 * M)
#     return {i**2 for i in range(1,bound+1)}


# def num_integer_solutions(M,perfect_squares):
#     count = 0
#     for w in range(1,M+1):
#         for l in range(w,M+1):
#             sq = (l+w)**2
#             for h in range(l,M+1):
#                 if (sq + h**2) in perfect_squares:
#                     count += 1
#         print(w/M)
#     return count

M = 5
m = 2
n = 1
explored_triples = set() # (3,4,5), (5,12,13), (6,8,10), (7, 10, ?)...

def f(target):
    global M, m, n, explored_triples
    while len(explored_triples) < target:
        # generate triple with a <= M
        while m**2 - n**2 <= M:
            if gcd(m, n) != 1:
                n -= 2
                continue

            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2

            print(a, b, c)
            explored_triples.add((a, b, c))

            n -= 2
            if n < 0:
                m += 1
                n = m-1

        print(explored_triples)
        # scale known triples so that tuple[0] <= M
        for triple in explored_triples.copy():
            k = 1
            while k * triple[0] < M:
                explored_triples.add(tuple(k*e for e in triple))
                k += 1
        M += 1

f(13)
print(explored_triples)




# def num_integer_solutions(M):
#     count = 0
#     for m in range(1,int(M**0.5)+1):
#         for n in range(m-1, 0, -2):
#             if gcd(m, n) != 1:
#                 continue

#             a = m**2 - n**2
#             b = 2*m*n
#             # c = m**2 + n**2

#             k = 1
#             # while k*a < M:
#             #     ka, kb, kc = k*a, k*b, k*c
                
#             #     k += 1


#             while k*a < M and k*b < 2*M:
#                 count += (k*b//2)-1
#                 k += 1
            
#             # while k*a < M:
#             #     count += (k*b//2)-1
#             #     k += 1

#     return count

# def first_over(goal):
#     M = 90
#     # perfect_squares = gen_perfect_squares(bound)
#     while num_integer_solutions(M) < goal:
#         M += 1
#     return M

# # print(first_over(1000000,bound=2000))
# # M_bound = 2000
# # perfect_squares = gen_perfect_squares(M)
# # print(first_over(2000))
# print(num_integer_solutions(100))