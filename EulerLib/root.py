class IntegerSquareRoot:
    def __init__(self,n:int,precision:int):
        self.n = n
        self.precision = precision
        self.__calculate()

    def __get_pairs(self):
        string = str(self.n)
        if self.offset%2 == 1:
            string = '0' + string
        return [int(string[i:i+2]) for i in range(0,len(string),2)]

    # Uses the algorithm described here: https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Decimal_(base_10)
    def __calculate(self):
        self.offset = len(str(self.n)) + len(str(self.n))%2
        self.value = []
        pairs = self.__get_pairs()
        c,p = 0,0
        for i in range(self.precision):
            c = c*100 + 0 if i >= len(pairs) else pairs[i]
            x = 0
            while x * (20*p + x) <= c:
                x += 1
            x -= 1
            self.value.append(x)
            y = x * (20*p + x)
            p = p * 10 + x
            c -= y
