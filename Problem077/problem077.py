# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 77

# What is the first value which can be written as the sum of primes in over five thousand different ways?
# Based on my solution to problem 76


from fishpy.primes import sieve


def count_sums(value,index,primes):
    if value < 0 or index >= len(primes):
        return 0
    if value == 0:
        return 1
    return count_sums(value,index+1,primes) + count_sums(value-primes[index],index,primes)

def first_over(count,max_prime):
    primes = sieve(max_prime)
    i = 2
    while count_sums(i,0,sorted(filter(lambda x: x <= i,primes))[::-1]) <= count:
        i += 1
    return i

print(first_over(5000,100))
