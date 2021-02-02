# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 74

# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?


from math import factorial as fact

def num_to_list(num):
    lst = []
    size = len(str(num))
    for i in range(size):
        lst.append(num // (10**(size-i-1)) % 10)
    return lst

def chain_step(n):
    return sum([fact(digit) for digit in num_to_list(n)])

def gen_factorial_chain(n):
    chain = [n]
    while (n := chain_step(n)) not in chain:
        chain.append(n)
    return chain

def find_len60_chains(max_,cycle_length):
    total = 0
    for i in range(1,max_):
        chain = gen_factorial_chain(i)
        if len(chain) == cycle_length:
            total += 1
    return total

print(find_len60_chains(1000000,60))