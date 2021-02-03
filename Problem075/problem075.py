# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 75

# Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple


from math import gcd

MAX_PERIMETER = int(1.5 * 10**6)

UPPER_M = 866
LOWER_M = 1
UPPER_N = 613
LOWER_N = 1

count_of_length = {}

for m in range(LOWER_M, UPPER_M):
    offset = 1 if (m + LOWER_N) % 2 == 0 else 0
    for n in range(LOWER_N + offset, m, 2):
        if gcd(m, n) != 1:
            continue

        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2

        sum_ = a + b + c
        k = 1
        while k*sum_ < MAX_PERIMETER:
            ka, kb, kc = k*a, k*b, k*c
            count_of_length[k*sum_] = 1 if k*sum_ not in count_of_length else count_of_length[k*sum_]+1
            k += 1

count = len([length for length in count_of_length if count_of_length[length] == 1])
print(count)