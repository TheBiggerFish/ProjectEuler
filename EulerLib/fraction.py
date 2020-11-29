from math import lcm,gcd

class Fraction:
    def __init__(self,numer,denom=1):
        self.n = numer
        self.d = denom
    
    def is_proper(self):
        return self.n < self.d

    def evaluate(self):
        return self.n / self.d

    def reciprocal(self):
        return Fraction(self.d,self.n)
    
    def add_int(self,num):
        return Fraction(self.n + (num * self.d),self.d)

    def __mul__(self,other):
        return Fraction(self.n*other.n,self.d*other.d)
    
    def __add__(self,other):
        lcd = Fraction.lcd(self,other)
        self_n = self.n * (lcd // self.d)
        other_n = other.n * (lcd // other.d)
        return Fraction(self_n + other_n,lcd)

    def __str__(self):
        return str(self.n) + '/' + str(self.d)
    
    def __lt__(self,other):
        return self.evaluate() < other.evaluate()

    def __gt__(self,other):
        return self.evaluate() > other.evaluate()

    @staticmethod
    def lcd(f1,f2):
        return lcm(f1.d,f2.d)

    def reduce(self):
        div = gcd(self.n,self.d)
        return Fraction(self.n//div,self.d//div)

    def hash(self):
        if self.n >= self.d:
            return self.n * self.n + self.n + self.d
        else:
            return self.d * self.d + self.n

class ContinuedFraction:
    def __init__(self,addend=0,numer=0,denom=None):
        self.a = addend #type:int
        self.n = numer #type:int
        self.d = denom #type:ContinuedFraction
        
    @staticmethod
    # Generate continued fraction using a continued fraction representation sequence.
    # The value x is used to generate the numerators of the continued fraction
    def gen_from_seq(seq,x=2):
        if len(seq) == 0:
            return ContinuedFraction(addend=0)

        frac = ContinuedFraction(addend=seq[-1])
        for num in reversed(seq[:-1]):
            if not isinstance(num,int) and not isinstance(num,float):
                raise TypeError
            frac.d = frac.copy()
            frac.n = x-1
            frac.a = num
        return frac
    
    # Determines the representation sequence of a continued fraction
    def get_seq(self):
        seq = [self.a]
        frac = self.d
        while frac is not None:
            seq.append(frac.a)
            frac = frac.d
        return seq

    # Adds a continued fraction to the end of a continued fraction. 
    def append(self,frac):
        recurse = self
        while recurse.d is not None:
            recurse = recurse.d
        recurse.d = frac
        return self

    def evaluate(self):
        if self.n == 0 or self.d is None:
            return float(self.a)
        return self.a + (self.n / self.d.evaluate())

    def reduce_fraction(self):
        if self.n == 0 or self.d is None:
            return Fraction(self.a)
        return (Fraction(self.n) * self.d.reduce_fraction().reciprocal()).add_int(self.a)

    @staticmethod
    # Generate a continued fraction representation sequence of length l for a square root of number n
    def gen_sqrt_seq(n,l):
        if (n**0.5).is_integer():
            return [n**0.5]
        m = 0
        d = 1
        a = int(n**0.5)
        seq = [a]
        while len(seq) < l:
            m = d * a - m
            d = (n - (m**2)) // d
            a = int(((n**0.5) + m) // d)
            seq.append(a)
        return seq

    def copy(self):
        return ContinuedFraction(addend=self.a,numer=self.n,denom=self.d)

    @property
    def a(self):
        return self.__a
        
    @property
    def n(self):
        return self.__n
    
    @property
    def d(self):
        return self.__d

    @a.setter
    def a(self, a):
        if not isinstance(a,int) and not isinstance(a,float):
            raise TypeError
        self.__a = a

    @n.setter
    def n(self, n):
        if not isinstance(n,int) and not isinstance(n,float):
            raise TypeError
        self.__n = n

    @d.setter
    def d(self, d):
        self.__d = d