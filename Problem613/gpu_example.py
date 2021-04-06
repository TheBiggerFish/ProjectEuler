#http://numba.pydata.org/numba-doc/0.35.0/cuda/random.html

from numba import cuda
from numba.cuda.random import create_xoroshiro128p_states, xoroshiro128p_uniform_float32
import numpy as np
import time
import random

@cuda.jit
def compute_pi(rng_states, iterations, out):
    """Find the maximum value in values and store in result[0]"""
    thread_id = cuda.grid(1)

    # Compute pi by drawing random (x, y) points and finding what
    # fraction lie inside a unit circle
    inside = 0
    for i in range(iterations):
        x = xoroshiro128p_uniform_float32(rng_states, thread_id)
        y = xoroshiro128p_uniform_float32(rng_states, thread_id)
        if x**2 + y**2 <= 1.0:
            inside += 1

    out[thread_id] = 4.0 * inside / iterations

threads_per_block = 32
blocks = 40
rng_states = create_xoroshiro128p_states(threads_per_block * blocks, seed=random.randint(1,2**64))
out = np.zeros(threads_per_block * blocks, dtype=np.float32)

start = time.perf_counter()
compute_pi[blocks, threads_per_block](rng_states, 100_000_000, out)
end = time.perf_counter()
print('pi:', out.mean())
print('time:',round(end-start,4))