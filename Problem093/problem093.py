# Written by Cameron Haddock and Daniel Millson
# Submitted as a solution to Project Euler's Problem 93

# By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.
# Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.
# Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.

NUM_DIGITS = 4
NUM_OPS = NUM_DIGITS-1

from fishpy.mathematics.arithmetic import Expression, PEMDAS, EvaluationDirection
from itertools import product, permutations

# permutations(range(0,10),NUM_DIGITS)
operations = list(product("*+/-", repeat=3))

parentheses_set = [
    "({} {} {} {} {} {} {})",
    "(({} {} {}) {} {}) {} {}",
    "({} {} ({} {} {})) {} {}",
    "{} {} (({} {} {}) {} {})",
    "{} {} ({} {} ({} {} {}))",
    "({} {} {}) {} {} {} {}",
    "{} {} ({} {} {}) {} {}",
    "{} {} {} {} ({} {} {})",
    "({} {} {}) {} ({} {} {})",
]

def intersperse(digits: list[int], ops: list[str]) -> list:
    result: list[str] = []
    for i, digit in enumerate(digits):
        result.append(digit)
        if i < len(ops):
            result.append(ops[i])
    return result

def generate_possible_results(digits: list[int]) -> set[int]:
    results: set[int] = set()
    for parens in parentheses_set:
        for ops in operations:
            for perm in permutations(digits):
                exp_string = parens.format(*intersperse(perm, ops))
                exp = Expression.build_from_string(exp_string, PEMDAS, EvaluationDirection.LEFT_TO_RIGHT)
                try:
                    value = float(exp.evaluate())
                except: 
                    continue
                if not value.is_integer() or value < 1:
                    continue
                results.add(int(value))
    return results

# print(exp.evaluate())

def is_increasing(digits) -> bool:
    for i in range(len(digits)-1):
        if digits[i] >= digits[i+1]:
            return False
    return True

def sequence_length(values: set[int]) -> int:
    i = 1
    while i in values:
        i += 1
    return i - 1


digit_list = list(filter(is_increasing, [list(map(int, str(num))) for num in range(10**(NUM_DIGITS-1),(10**NUM_DIGITS))]))
# digit_list=[[1,2,3,4]]

highest = [0] * NUM_DIGITS
highest_value = 0
for digits in digit_list:
    results = generate_possible_results(digits)
    length = sequence_length(results)
    if length > highest_value:
        highest_value = length
        highest = digits

print(highest_value, highest)


