# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 613

# Dave is doing his homework on the balcony and, preparing a presentation about Pythagorean triangles, has just cut out a triangle with side lengths 30cm, 40cm and 50cm from some cardboard, when a gust of wind blows the triangle down into the garden.
# Another gust blows a small ant straight onto this triangle. The poor ant is completely disoriented and starts to crawl straight ahead in random direction in order to get back into the grass.
# Assuming that all possible positions of the ant within the triangle and all possible directions of moving on are equiprobable, what is the probability that the ant leaves the triangle along its longest side?
# Give your answer rounded to 10 digits after the decimal point.


import random
import threading
import time
from math import cos, pi, sin
from typing import List

from fishpy.geometry import Point, Triangle

ITERATIONS = 10**6
THREADS = 8
MAX_Y = 3*10**6
MAX_X = 4*10**6
STEP_SIZE = 10**5
slope_func = lambda x: -3 * x / 4 + MAX_Y

total_top = 0
top_lock = threading.Lock()
total_left = 0
left_lock = threading.Lock()
total_bottom = 0
bottom_lock = threading.Lock()


def disoriented_ant(slope_func,iterations):
    start = time.perf_counter()
    global total_bottom,total_left,total_top
    top,left,bottom = 0,0,0
    for _ in range(iterations):
        x = random.uniform(0,MAX_X)
        y = random.uniform(0,slope_func(x))
        while 0 < x < MAX_X and 0 < y < slope_func(x):
            rand_angle = random.uniform(0,2*pi)
            x += cos(rand_angle) * STEP_SIZE
            y += sin(rand_angle) * STEP_SIZE
        if x < 0 and 0 < y < MAX_Y:
            left += 1
        elif 0 < x < MAX_X and y < 0:
            bottom += 1
        elif y > slope_func(x):
            top += 1
    end = time.perf_counter()
    print(f'Thread {threading.current_thread().name} found top={top}, left={left}, bottom={bottom} in {round(end-start,2)} seconds')
    bottom_lock.acquire()
    total_bottom += bottom
    bottom_lock.release()
    left_lock.acquire()
    total_left += left
    left_lock.release()
    top_lock.acquire()
    total_top += top
    top_lock.release()

threads:List[threading.Thread] = []
for t in range(THREADS):
    threads.append(threading.Thread(target=disoriented_ant,name=f't{t}',args=[slope_func,ITERATIONS//THREADS]))

start = time.perf_counter()
for t in threads:
    t.start()
for t in threads:
    t.join()
end = time.perf_counter()


total = sum((total_top,total_left,total_bottom))
print(f'Counts: Top={total_top}, Left={total_left}, Bottom={total_bottom} in {round(end-start,2)} seconds')
print(f'Rates: Top={round(total_top/total,8)}, Left={round(total_left/total,8)}, Bottom={round(total_bottom/total,8)}')
