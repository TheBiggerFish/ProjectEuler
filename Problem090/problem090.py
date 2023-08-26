# Written by Cameron Haddock and Daniel Millson
# Submitted as a solution to Project Euler's Problem 90

# How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?


from itertools import combinations

constraints = [
    (0, 1),
    (0, 4),
    (0, 6),
    (1, 6),
    (2, 5),
    (3, 6),
    (4, 6),
    (1, 8),
]


def meets_constraint(die1, die2, constraint: tuple[int, int]) -> bool:
    if constraint[0] in die1 and constraint[1] in die2:
        return True
    if constraint[0] in die2 and constraint[1] in die1:
        return True
    return False


def apply_constraints(die1: set[int], die2: set[int]) -> bool:
    for die in (die1, die2):
        if 9 in die:
            die.remove(9)
            die.add(6)
    for constraint in constraints:
        if not meets_constraint(die1, die2, constraint):
            return False
    return True


dice = list(combinations(range(0, 10), 6))
pairs = []
for i, die1 in enumerate(dice):
    for _, die2 in enumerate(dice[i+1:]):
        pairs.append((set(die1), set(die2)))

pairs = list(filter(lambda pair: apply_constraints(pair[0], pair[1]), pairs))

print(len(pairs))
