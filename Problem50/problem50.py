# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 50

# The prime 41, can be written as the sum of six consecutive primes:
#   41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

    
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    for divisor in range(6, min(int(n**0.5) + 6,n-1), 6):
        if n % (divisor - 1) == 0 or n % (divisor + 1) == 0:
            return False
    return True

def gen_primes(max_):
    lst = [2,3]
    for i in range(6, max_, 6):
        if is_prime(i-1):
            lst.append(i-1)
        if is_prime(i+1):
            lst.append(i+1) 
    return lst

def con_primes(max_):
    primes = gen_primes(max_)
    longest = []
    for i in range(len(primes)-len(longest)):
        for j in range(i+len(longest)+1,len(primes)):
            subset = primes[i:j+1] 
            sum_ = sum(subset)
            if sum_ > max_ or sum_ < sum(longest):
                break
            if is_prime(sum_):
                if len(subset) > len(longest):
                    longest = subset.copy()
    return longest

print(sum(con_primes(1000000)))