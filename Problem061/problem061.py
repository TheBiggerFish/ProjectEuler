# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 61

# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.


def preceeds(left,right):
    return left % 100 == right // 100

def figurate_nums(cycle,used_sets,figures):
    if len(cycle) == 6:
        if preceeds(cycle[-1],cycle[0]):
            return cycle
        return None
    for fig in figures:
        if fig not in used_sets:
            for i in figures[fig]:
                if len(cycle) == 0 or preceeds(cycle[-1],i):
                    recur = figurate_nums(cycle + [i],used_sets | {fig},figures)
                    if recur is not None:
                        return recur
    return None

def figurate_wrapper(digits):
    filter_func = lambda n: 10**(digits-1) <= n < 10**digits
    figures = {
        3: set(filter(filter_func,[n*(n+1)//2 for n in range(10**(digits-1))])),
        4: set(filter(filter_func,[n**2 for n in range(10**(digits-1))])),
        5: set(filter(filter_func,[n*(3*n-1)//2 for n in range(10**(digits-1))])),
        6: set(filter(filter_func,[n*(2*n-1) for n in range(10**(digits-1))])),
        7: set(filter(filter_func,[n*(5*n-3)//2 for n in range(10**(digits-1))])),
        8: set(filter(filter_func,[n*(3*n-2) for n in range(10**(digits-1))]))
    }
    return sum(figurate_nums(list(),set(),figures))

print(figurate_wrapper(4))