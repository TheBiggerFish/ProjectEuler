# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 100

# If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21) * (14/20) = 1/2.
# The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
# By finding the first arrangement to contain over 10^12 discs in total, determine the number of blue discs that the box would contain.

import numpy as np
from numba import cuda

BLOCKS = (96, 32)


@cuda.jit
def compute_pi(iterations, result):
    START = 10**12
    RATIO = 0.5 ** 0.5

    thread_id = cuda.grid(1)

    blue = np.uint64(RATIO * START) + thread_id
    red = np.uint64((1-RATIO) * START)

    i = 0
    while result[0] == 0:
        n = blue * (blue - 1)
        d = (blue + red) * (blue + red - 1)

        n2 = n << 1

        if n2 == d:
            result[0] = blue
            result[1] = red
        elif n2 < d:
            blue += BLOCKS[0] * BLOCKS[1]
        elif n2 > d:
            red += 1
        i += 1
        if i == iterations:
            result[0] = n2
            result[1] = d
            break


out = np.zeros(2, dtype=np.int64)
compute_pi[BLOCKS[0], BLOCKS[1]](1_000_000_000, out)
print("FOUND:", out[0], out[1])
