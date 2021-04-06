# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 205

#Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
#Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
#Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.
#What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg


from numba import cuda
from numba.cuda.random import create_xoroshiro128p_states as create_rand_states, xoroshiro128p_uniform_float32 as random_from_states
import numpy as np
import random
import time

n = 2**40
blocks = 20
threads_per_block = 64
total_threads = threads_per_block * blocks

@cuda.jit
def probability(rng_states, iterations, out):
    thread_id = cuda.grid(1)
    d4_count = 9
    d6_count = 6

    win4 = 0
    for i in range(iterations):
        d4,d6 = 0,0
        for _ in range(d4_count):
            d4 += int(random_from_states(rng_states,thread_id)*4)+1
        for _ in range(d6_count):
            d6 += int(random_from_states(rng_states,thread_id)*6)+1
        if d4 > d6:
            win4 += 1
    out[thread_id] = win4


rng_states = create_rand_states(total_threads, seed=random.randint(1,2**64))
out = np.zeros(total_threads, dtype=np.int64)

start = time.perf_counter()
probability[blocks, threads_per_block](rng_states, n/total_threads, out)
end = time.perf_counter()

# print('Number of Iterations:',n)
# print('Sum:', out.sum())
print('Probability:', out.sum()/n)
print('time:',round(end-start,4))