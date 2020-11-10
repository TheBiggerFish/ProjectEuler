# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 21

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.


def factor(number):
    f = {1,number}
    sqr = int(number**0.5) + 1
    for divisor in range(2, sqr):
        if number % divisor == 0:
            f.add(divisor)
            f.add(int(number/divisor))
    return sorted(f)

def get_amicable(number):
    num_sum = sum(factor(number)) - number
    if num_sum == number:
        return -1
    if number == sum(factor(num_sum)) - num_sum:
        return num_sum
    return -1

def all_amicable(max_):
    amicables = set()
    for i in range(2,max_):
        if i in amicables:
            continue
        rv = get_amicable(i)
        if rv != -1:
            amicables.add(i)
            amicables.add(rv)
    return amicables

print(sum(all_amicable(10000)))