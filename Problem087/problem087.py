# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 85

# How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?


from EulerLib.functions.primes import sieve

def num_sums_below(sum_bound,prime_bound):

    primes = sieve(prime_bound)
    primes_2 = set(filter(lambda x: x <= sum_bound**(1/2),primes))
    primes_3 = set(filter(lambda x: x <= sum_bound**(1/3),primes))
    primes_4 = set(filter(lambda x: x <= sum_bound**(1/4),primes))
    
    found = set()
    for square in primes_2:
        for cube in primes_3:
            for quad in primes_4:
                if (sum_ := square**2 + cube**3 + quad**4) < sum_bound:
                    found.add(sum_)
    return len(found)

print(num_sums_below(5*10**7,10000))