from frozendict import frozendict
from math import prod

class FactorFactory:
    def __init__(self):
        self.primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                       43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                       101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 
                       151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 
                       199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 
                       263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 
                       317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 
                       383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
                       443, 449, 457, 461, 463, 467, 479, 487, 491, 499}
        self.factors: dict[int, set[frozendict[int, int]]] = {}

    def _is_known_prime(self, number: int) -> bool:
        return number in self.primes

    def _factor_helper(self, number: int, start: int) -> set[frozendict[int, int]]:
        result: set[frozendict[int, int]] = set()
        if number <= 1:
            return result
        elif self._is_known_prime(number):
            result.add(frozendict({number: 1}))
            return result

        for i in range(start, number+1):
            if number % i == 0:
                factorings = self._factor_helper(number//i, i)
                for factoring in factorings:
                    result.add(factoring.set(i, factoring.get(i, 0) + 1))
        if start == 2 and len(result) == 0:
            self.primes.add(number)
        if number > start:
            result.add(frozendict({number: 1}))

        self.factors[number] = result
        return result

    def factor(self, number: int) -> set[frozendict[int, int]]:
        return self._factor_helper(number, 2)

    @staticmethod
    def flatten(factors: set[frozendict[int, int]]) -> list[str]:
        result: list[str] = []
        for factoring in factors:
            line = ''
            for key in sorted(factoring.keys()):
                line += 'x'.join([str(key)]*factoring[key]) + 'x'
            result.append(line.rstrip('x'))
        return result

    @staticmethod
    def to_list(factoring: frozendict[int, int]) -> list[int]:
        result: list[int] = []
        for factor, counts in factoring.items():
            result += [factor]*counts
        return result


def minimal(length: int, factory: FactorFactory):
    min_ = 2*length
    for i in range(length, 2*length):
        for factoring in factory.factor(i):
            factor_list = FactorFactory.to_list(factoring)
            product = prod(factor_list)
            if product == sum(factor_list) + (length - len(factor_list)):
                min_ = min(product, min_)
    return min_

def product_sum(max_: int) -> int:
    factory = FactorFactory()
    terms: set[int] = set()
    for k in range(2, max_+1):
        terms.add(minimal(k, factory))
    return sum(terms)


def main():
    sum_ = product_sum(200)
    print(f'Total sum: {sum_}')


if __name__ == '__main__':
    main()
