# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 58

# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
#       37 36 35 34 33 32 31
#       38 17 16 15 14 13 30
#       39 18  5  4  3 12 29
#       40 19  6  1  2 11 28
#       41 20  7  8  9 10 27
#       42 21 22 23 24 25 26
#       43 44 45 46 47 48 49
# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    for divisor in range(6, min(int(n**0.5) + 6,n-1), 6):
        if n % (divisor - 1) == 0 or n % (divisor + 1) == 0:
            return False
    return True

def diagonal_primes(ratio):
    primes = 3
    diagonals = 5
    i = 9
    step = 4
    while primes/diagonals >= ratio:
        for _ in range(4):
            i += step
            if is_prime(i):
                primes += 1
            diagonals += 1
        step += 2
    print(primes,diagonals)
    return step - 1

print(diagonal_primes(1/10))