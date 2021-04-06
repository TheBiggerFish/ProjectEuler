# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 613

# Dave is doing his homework on the balcony and, preparing a presentation about Pythagorean triangles, has just cut out a triangle with side lengths 30cm, 40cm and 50cm from some cardboard, when a gust of wind blows the triangle down into the garden.
# Another gust blows a small ant straight onto this triangle. The poor ant is completely disoriented and starts to crawl straight ahead in random direction in order to get back into the grass.
# Assuming that all possible positions of the ant within the triangle and all possible directions of moving on are equiprobable, what is the probability that the ant leaves the triangle along its longest side?
# Give your answer rounded to 10 digits after the decimal point.


from __future__ import print_function, absolute_import

from numba import cuda
from numba.cuda.random import create_xoroshiro128p_states, xoroshiro128p_uniform_float32
from math import pi,cos,sin
import numpy as np
import time
import random

ITERATIONS = 1028 * 10**3
BLOCKS = 40
THREADS_PER_BLOCK = 32 #1280 cores / 40 blocks = 32 cores per block
PRECISION = 10**3
MAX_Y = 30 * PRECISION
MAX_X = 40 * PRECISION
STEP_SIZE = PRECISION / 10


@cuda.jit
def disoriented_ant(rng_states,iterations,out):
    slope_func = lambda x: -3 * x / 4 + MAX_Y
    thread_id = cuda.grid(1)
    top = 0

    for _ in range(iterations):
        x = 1
        y = 1
        x = int(xoroshiro128p_uniform_float32(rng_states,thread_id)*(MAX_X+1))
        y = int(xoroshiro128p_uniform_float32(rng_states,thread_id)*(slope_func(x)+1))
        while 0 < x < MAX_X and 0 < y < slope_func(x):
            rand_angle = int(xoroshiro128p_uniform_float32(rng_states,thread_id)*(2*pi))
            x += cos(rand_angle) * STEP_SIZE
            y += sin(rand_angle) * STEP_SIZE
        if y > slope_func(x):
            top += 1

    out[thread_id] = top

rng_states = create_xoroshiro128p_states(THREADS_PER_BLOCK * BLOCKS, seed=random.randint(1_000_000_000,2_147_483_647))
out = np.zeros(THREADS_PER_BLOCK * BLOCKS, dtype=np.uint64)

start = time.perf_counter()
disoriented_ant[BLOCKS,THREADS_PER_BLOCK](rng_states,ITERATIONS//(THREADS_PER_BLOCK*BLOCKS), out)
end = time.perf_counter()
print('Total sum:', out.sum()/ITERATIONS)
print('time:',round(end-start,4))