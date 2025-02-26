from functools import lru_cache

CELLS = 50
MIN_SIZE = 3

@lru_cache
def combinations(cellCount: int):
    if cellCount < 0:
        return 1
    
    total = 1
    for size in range(MIN_SIZE, cellCount + 1):
        for pos in range(0, cellCount - size + 1):
            right = cellCount - size - pos - 1
            total += combinations(right)
    return total

results = combinations(CELLS)
print(results)