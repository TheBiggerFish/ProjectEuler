# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 78

# Find the least value of n for which p(n) is divisible by one million.


# https://en.wikipedia.org/wiki/Partition_function_(number_theory)#Recurrence_relations
def partition(n,partitions):
    k = 1
    sum_ = 0
    while n - (k * (3*k - 1) / 2) >= 0:
        sum_ += int(partitions[n - (k * (3*k - 1) / 2)]) * int((-1)**(k+1))
        if k < 0:
            k -= 1
        k = -k
    return sum_

def first_partition_divisible_by(divisor):
    partitions = {0:1}
    i = 1
    while (rv := partition(i,partitions)) % divisor != 0:
        partitions[i] = rv
        i += 1
    return i

print(first_partition_divisible_by(1000000))