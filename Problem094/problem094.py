# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 94


MAX_PERIMETER = 10**9

n = 5
perim = 16 # perim of 5,5,6
sum_ = 0
delta = -1

prev = 1

while perim <= MAX_PERIMETER:
    sum_ += perim
    prev, n = n, 4 * n - prev + 2*delta
    perim = 3*n + delta
    delta = -delta
print(sum_)