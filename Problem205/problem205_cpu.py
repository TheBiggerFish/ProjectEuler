# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 205

#Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
#Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
#Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.
#What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg


from EulerLib.debug import timer
import threading
import random

n = 2**20
num_threads = 16
n_per_thread = n // num_threads
results = [None] * num_threads

@timer
def probability(n,thread_id):
    wins4,wins6 = 0,0
    for _ in range(n):
        d4 = sum(random.randint(1,4) for _ in range(9))
        d6 = sum(random.randint(1,6) for _ in range(6))
        if d4 > d6:
            wins4 += 1
    results[thread_id] = {'wins4':wins4,'wins6':wins6}
    print(f'Thread {thread_id}={wins4},{wins6}')

threads = []
for i in range(num_threads):
    threads.append(threading.Thread(target=probability, args=[n_per_thread,i], name='t'+str(i)))

for t in threads:
    t.start()

for t in threads:
    t.join()

print(sum(map(lambda p: p['wins4'], results))/n)