import numpy as np
from math import log, floor, ceil, log10
from fishpy.utility.debug import monitor, timer, profile
from decimal import getcontext, Decimal

MAX_N = 5_000_000
ctx = getcontext()

def log_base_r_floor(n: Decimal) -> int:
    if n < 1:
        arr = neg_r_pows
        low = -len(arr)
        high = -1
    else:
        arr = pos_r_pows
        low = 0
        high = len(arr) - 1
    if arr[high] < n:
        return high
    while high > low:
        mid = (low + high) // 2

        if round(arr[mid]-n, ctx.prec//2) == 0:
            return mid
        elif arr[mid] > n:
            high = mid - 1
        elif arr[mid + 1] <= n:
            low = mid + 1
        elif arr[mid] <= n and arr[mid+1] > n:
            return mid
    mid = (low + high) // 2
    if arr[mid + 1] < n:
        return mid + 1
    elif arr[mid] < n:
        return mid
    
    print("FALLBACK")
    return true_log_base_r_floor(n)

def true_log_base_r_floor(n: Decimal) -> int:
    exp = n.log10() / r_log10
    if round(exp, ctx.prec//2) % 1 == 0:
        exp = round(exp)
    return floor(exp)


def eval_r() -> Decimal:
    return (Decimal(1) + 
     ctx.power(Decimal(0.5) * (Decimal(29)-Decimal(3)*ctx.power(Decimal(93),Decimal(0.5))), Decimal(1)/Decimal(3)) + 
     ctx.power(Decimal(0.5) * (Decimal(29)+Decimal(3)*ctx.power(Decimal(93),Decimal(0.5))), Decimal(1)/Decimal(3))) / Decimal(3)


@monitor
def get_terms(n):
    n = Decimal(n)
    exponents = []
    while n > 0:
        exponent = true_log_base_r_floor(n)
        exponents.append(exponent)
        n -= r**exponent
        if round(n, ctx.prec//2) == 0:
            break
    return exponents

def w(n):
    return len(get_terms(n))

# @profile
def S(m):
    total = 0
    for i in range(1, m+1):
        total += w(i**2)
    return total

def problem(n, prec):
    ctx.prec = prec
    
    global r, r_log10, pos_r_pows, neg_r_pows
    r = eval_r()
    r_log10 = r.log10()

    pos_r_pows = [r**e for e in range(0, true_log_base_r_floor(Decimal(n)**2) + 1)]
    neg_r_pows = [r**e for e in range(true_log_base_r_floor(Decimal(10)**-prec), 0)]

    print(S(n)) 

problem(10, 20)  # S(10) = 61
# problem(100, 24)  # S(100) = 1206
# problem(1000, 24)  # S(1000) = 19403
# problem(5_000_000, 64)
