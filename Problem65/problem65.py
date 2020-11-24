# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 65

# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.


class Fraction:
    def __init__(self,numer,denom=1):
        self.n = numer
        self.d = denom
    
    def __str__(self):
        return str(self.n) + '/' + str(self.d)

    def reciprocal(self):
        return Fraction(self.d,self.n)
    
    def add_int(self,num):
        return Fraction(self.n + (num * self.d),self.d)

    @staticmethod
    def generate_from_sequence(seq):
        frac = Fraction(seq[-1])
        for num in seq[:-1][::-1]:
            frac = frac.reciprocal()
            frac = frac.add_int(num)
        return frac

def gen_e(digits):
    lst = [2]
    for i in range(digits-1):
        if i % 3 == 1:
            lst.append(2*((i//3)+1))
        else:
            lst.append(1)
    return lst

print(sum([int(c) for c in str(Fraction.generate_from_sequence(gen_e(100)).n)]))