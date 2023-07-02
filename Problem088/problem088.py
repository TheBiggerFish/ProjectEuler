from frozendict import frozendict


class FactorFactory:
    def __init__(self):
        self.primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                       43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        self.factors: dict[int, set[frozendict[int, int]]] = {}

    def _is_known_prime(self, number: int) -> bool:
        return number in self.primes

    def _factor_helper(self, number: int, start: int) -> set[frozendict[int, int]]:
        print(number, start)
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


def main():
    factory = FactorFactory()
    factors = factory.factor(100)
    print(FactorFactory.flatten(factors))


if __name__ == '__main__':
    main()
