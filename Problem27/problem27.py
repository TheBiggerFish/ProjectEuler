# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 27

# Find the product of the coefficients, a and b, for the quadratic expression n^2 + an + b that produces the maximum number of primes for consecutive values of n, starting with n=0.


def is_prime(n):
    if n <= 1:
        return False
    sqr = int(n**0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def get_consec_primes(a,b):
    n = 1
    while is_prime(n**2+a*n+b):
        n += 1
    return n

def quadratic_generator(max_a,max_b):
    max_run=0
    max_value=1
    for i in [2]+list(range(3,max_b+1,2)):
        if not is_prime(i):
            continue
        for j in range(max_a+1):
            for sign in range(4):
                if sign == 0:
                    a = j
                    b = i
                if sign == 1:
                    a = j
                    b = -i
                elif sign == 2:
                    a = -j
                    b = i
                elif sign == 3:
                    a = -j
                    b = -i
                rv = get_consec_primes(a,b)
                if rv > max_run:
                    max_run = rv
                    max_value = a*b
    return max_value

print(quadratic_generator(1000,1000))