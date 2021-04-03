# Written by Cameron Haddock and Daniel Millson
# Submitted as a solution to Project Euler's Problem 634

# Define F(n) to be the number of integers x <= n that can be written in the form x = a^2 * b^3, where a and b are integers not necessarily different and both greater than 1.
# Find F(9 x 10^18).

# from EulerLib.debug import profile,timer
import numpy as np
import threading
from math import log

n = 9*10**18
highest = int(n**(1/5))+1
print(n)
num_threads = 8
precision = 8

s = set()
# sets = []

# @timer
# In other words, for each input a, how many possible b values exist
def search(low, high, ind):
    # a**2 * b**3
    
    for a in range(low, high):   # n//8+1
        p = a**2
        if p > n:
            break
        for b in range(a, int((n/p)**(1/3))+1):      # n//4+1
            q = b**3
            x = p * q
            if x > n:
                break
            s.add(np.uint64(x))
    # a**3 * b**2
    for a in range(low, high):        # n//4+1
        p = a**3
        if p > n:
            break
        for b in range(a, int((n/p)**(1/2))+1): # n//8+1
            q = b**2
            x = p * q
            if x > n:
                break
            s.add(np.uint64(x))

    # print(threading.current_thread().name, len(sets[ind]),low,high)
    print(threading.current_thread().name,low,high)

threads = []
splits = [(i**precision/num_threads)+i**(precision-1) for i in range(num_threads+1)]
splits = [int(num/max(splits)*highest) for num in splits]

for t in range(num_threads):
    # sets.append(set())
    splits[t],splits[t+1] = max(2,splits[t]),max(2,splits[t+1])
    if splits[t+1] <= splits[t]:
        splits[t+1] += splits[t] - splits[t+1] + 1
    # print(max(2,t*(n//num_threads)), (t+1)*(n//num_threads))
    # low = max(2,int(log(t+1)*(highest//num_threads)))
    # high = int(log(t+2)*(highest//num_threads))+1
    low = max(2, splits[t])
    high = max(2, splits[t+1])
    print(low,high)
    threads.append(threading.Thread(target=search, args=(low, high, t), name='t'+str(t)))

for t in threads:
    t.start()

for t in threads:
    t.join()

# print('Combining sets')
# for t in range(num_threads):
#     s = s | sets[t]
#     print('Deleting set:',t)
#     del sets[t]

# print('Individuals:',len(s))
# duplicates = sum([len(count) for count in sets]) - len(s)
# print('Duplicates:',duplicates)
print(len(s))