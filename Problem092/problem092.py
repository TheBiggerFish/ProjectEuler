# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 92

# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before. How many starting numbers below ten million will arrive at 89?

def next_in_chain(n):
    return sum([int(digit)**2 for digit in str(n)])

def square_chain(max_):
    found = set()
    count = 0
    for i in range(1,max_):
        n = i
        while n != 1 and n != 89 and n not in found:
            n = next_in_chain(n)
        if n == 89 or n in found:
            found.add(i)
            count += 1
    return count

print(square_chain(10**7))