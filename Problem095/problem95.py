# Written by Cameron Haddock and Daniel Millson
# Submitted as a solution to Project Euler's Problem 95

# Find the smallest member of the longest amicable chain with no element exceeding one million.

from functools import lru_cache
from typing import Generator


def divisorGenerator(n: int) -> Generator[int, None, None]:
    largerFactors: list[int] = []
    for i in range(1, int((n**0.5)+1)):
        if n % i == 0:
            yield i
            if i*i != n:
                largerFactors.append(int(n / i))

    for f in reversed(largerFactors):
        yield f
    yield n


@lru_cache
def properDivisors(n: int) -> set[int]:
    divisors = set(divisorGenerator(n))
    divisors.remove(n)
    return divisors


def main():
    BOUND = 1_000_000
    seen: set[int] = set()
    longestChain: set[int] = set()

    for num in range(BOUND):
        loop: set[int] = {num}
        next_ = num
        while True:
            next_ = sum(properDivisors(next_))
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
    print(f'Smallest value in longest chain: {min(longestChain)}')


if __name__ == "__main__":
    main()
