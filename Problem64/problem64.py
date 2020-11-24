# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 64

# How many continued fractions for N <= 10000 have an odd period?


class Iteration:
    def __init__(self,S):
        self.S = S
        self.m = 0
        self.d = 1
        self.a = int(S**0.5)

    def iterate(self):
        self.m = self.d * self.a - self.m
        self.d = (self.S - (self.m**2)) // self.d
        self.a = int(((self.S**0.5) + self.m) // self.d)
        return self

    def __eq__(self,other):
        return self.S == other.S and self.m == other.m and self.d == other.d and self.a == other.a

    def copy(self):
        other = Iteration(self.S)
        other.m,other.d,other.a = self.m,self.d,self.a
        return other

    @staticmethod
    def whole(S):
        return S**0.5 - int(S**0.5) == 0

def get_period(S):
    period = []
    fraction = Iteration(S)
    while fraction.iterate() not in period:
        period.append(fraction.copy())
    return len([fraction.a for fraction in period])

def root_odd_cycle(max_):
    odds = 0
    for i in range(2,max_+1):
        if not Iteration.whole(i):
            if get_period(i) % 2 == 1:
                odds += 1
    return odds

print(root_odd_cycle(10000))