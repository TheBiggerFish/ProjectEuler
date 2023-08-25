from typing import Generator
from math import sqrt

def divisorListGenerator(n:int) -> Generator:
    largerFactors = []
    for i in range(1, int((n)+1)):
        if n % i == 0:
            yield i
            if i*i != n:
                largerFactors.append(int(n / i))
    
    for f in reversed(largerFactors):
        yield f
    yield n

def divisorList(n:int) -> set[int]:
    return set(divisorListGenerator(n))

def properDivisorList(n:int) -> set[int]:
    divisors = divisorList(n)
    divisors.remove(n)
    return divisors

BOUND = 1_000_000
seen: set[int] = set()
longestChain: set[int] = set()

for num in range(BOUND):
    loop: set[int] = {num}
    next_ = num
    while True:
        next_ = sum(properDivisorList(next_))
        if next_ in seen or next_ >= BOUND:
            break
        if next_ == num:
            print(loop)
            if len(loop) > len(longestChain):
                longestChain = loop
            seen = seen | loop
            break
        if next_ in loop:
            break    
        loop.add(next_)

print(longestChain)
