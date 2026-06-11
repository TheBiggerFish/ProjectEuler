# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 829

# We define M(n) to be the smallest number that has a factor tree identical in shape to the factor tree for n!!, the double factorial of n.
# Find the sum from n=2 to 31 of M(n)

from math import prod

from fishpy.mathematics.primes import sieve
from fishpy.structures import BinaryTree
from fishpy.utility import timer

PRIMES = sieve(1_000_000)


def double_factorial(n: int) -> int:
    return prod(i for i in range(n, 1, -2))


def optimal_factors(n: int) -> tuple[int, int]:
    start = int(n**0.5)
    for i in range(start, 1, -1):
        if n % i == 0:
            return i, n // i
    return 1, n


def build_factor_tree(n: int) -> BinaryTree:
    root = BinaryTree(n)
    l_val, r_val = optimal_factors(n)
    if l_val == 1 and r_val == n:
        return root
    root.left = build_factor_tree(l_val)
    root.right = build_factor_tree(r_val)
    return root


def build_same_structure(structure: BinaryTree, min_value: int = 2) -> BinaryTree:
    if structure.is_leaf():
        n = min_value
        while n not in PRIMES:
            n += 1
        return BinaryTree(n)
    elif (structure.value & -structure.value) == structure.value:
        # is power of 2, already min
        return structure

    left = build_same_structure(structure.left, min_value)
    right = structure.right
    while True:
        right = build_same_structure(structure.right, min_value)
        if right.value >= left.value:
            break
        min_value += 1
    return BinaryTree(left.value * right.value, left, right)


@timer
def M(n: int):
    treeM = build_factor_tree(double_factorial(n))
    treeSame = build_same_structure(treeM, 2)
    return treeSame.value

def main():
    # t = build_factor_tree(double_factorial(9))
    # t2 = build_same_structure(t, 2)
    # print(t2)
    # print(M(9))
    sum_ = 0
    for n in range(2, 31+1):
        sum_ += (m := M(n))
        print(f'M({n})={m}')
    print(f'Sum(M(n))={sum_}')


if __name__ == '__main__':
    main()

# Don't actually need to factor anything. We're using a factorial, so we already know all the factors. Try to recursively partition the factors to be the closest to each other.
