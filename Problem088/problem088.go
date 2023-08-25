package main

import (
	"fmt"
)

type FactorGenerator struct {
	factors map[int][][]int
	primes  map[int]bool
}

func (generator *FactorGenerator) IsPrime(n int) bool {
	prime, found := generator.primes[n]
	return found && prime
}

func (generator *FactorGenerator) factorHelper(n int, start int) [][]int {
	// fmt.Printf("n=%d, start=%d\n", n, start)
	var result [][]int

	if n <= 1 {
		return [][]int{}
	} else if cached, found := generator.factors[n]; found {
		for _, factors := range cached {
			if factors[len(factors)-1] >= n {
				result = append(result, factors)
			}
		}
		return result
	} else if generator.IsPrime(n) {
		return append(result, []int{n})
	} else if start*start > n {
		return append(result, []int{n})
	}

	for i := start; i*i <= n; i++ {
		if n%i == 0 {
			// fmt.Printf("n=%d, i=%d\n", n, i)
			recursion := generator.factorHelper(n/i, i)
			for _, value := range recursion {
				result = append(result, append(value, i))
			}
		}
	}

	if len(result) == 0 {
		generator.primes[n] = true
	}
	result = append(result, []int{n})

	// fmt.Printf("n=%d, result=%d\n", n, len(result))
	generator.factors[n] = result

	return result
}

func (generator *FactorGenerator) Factor(n int) [][]int {
	return generator.factorHelper(n, 2)
}

func sum(list []int) int {
	sum := 0
	for _, term := range list {
		sum += term
	}
	return sum
}

func productSum(k int, generator FactorGenerator) int {
	// var max int
	// if k%2 == 0 {
	// 	max = k * 2
	// } else {
	// 	max = math.MaxInt - 1
	// }

	for i := k; i <= 20; i++ {
		fmt.Printf("k=%d, i=%d\n", k, i)
		if generator.IsPrime(i) {
			continue
		}
		factors := generator.Factor(i)
		fmt.Println(i, factors)
		for _, factoring := range factors {
			// fmt.Println(k, i, factoring, sum(factoring), (k - len(factoring)))
			if sum(factoring)+(k-len(factoring)) == i {
				return i
			}
		}
	}

	return -1
}

func main() {
	generator := FactorGenerator{make(map[int][][]int), make(map[int]bool)}
	minimal := make(map[int]bool) // set of ints
	for i := 2; i <= 5; i++ {
		value := productSum(i, generator)
		fmt.Printf("productSum(%d) = %d\n", i, value)
		minimal[value] = true
	}

	sum := 0
	for value := range minimal {
		sum += value
	}

	fmt.Printf("minimal product-sum = %d\n", sum)
}
