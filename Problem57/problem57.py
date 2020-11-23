# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 57

# In the first one-thousand expansions of sqrt(2), how many fractions contain a numerator with more digits than the denominator?


import sys

class Fraction:
    def __init__(self,numer,denom=1):
        self.n = numer
        self.d = denom
    
    def reciprocal(self):
        return Fraction(self.d,self.n)
    
    def add_int(self,num):
        self.n += num * self.d

    def __mul__(self,other):
        return Fraction(self.n*other.n,self.d*other.d)
    
    def __add__(self,other):
        lcd = Fraction.lcd(self,other)
        self_n = self.n * (lcd // self.d)
        other_n = other.n * (lcd // other.d)
        return Fraction(self_n + other_n,lcd)

    def __str__(self):
        return str(self.n) + '/' + str(self.d)

    @staticmethod
    def lcd(f1,f2):
        a,b = f1.d,f2.d
        while b > 0:
            a, b = b, a % b
        return f1.d * f2.d // a

def sqrt_two(max_depth,depth=0):
    if depth >= max_depth:
        return Fraction(2)
    if depth == 0:
        return sqrt_two(max_depth,depth+1).reciprocal() + Fraction(1)
    return sqrt_two(max_depth,depth+1).reciprocal() + Fraction(2)

def find_big_numer(iter):
    count = 0
    for i in range(1,iter):
        frac = sqrt_two(i)
        if len(str(frac.n)) > len(str(frac.d)):
            count += 1
    return count 

sys.setrecursionlimit(1500)
print(find_big_numer(1000)) # Deepest I can go before max depth recursion fails