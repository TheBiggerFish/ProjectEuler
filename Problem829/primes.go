//go:build ignore

package main

import (
	"bufio"
	"bytes"
	"encoding/binary"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func upperBoundForNthPrime(n int) int {
	if n < 6 {
		return 15
	}
	x := float64(n)
	return int(math.Ceil(x*(math.Log(x)+math.Log(math.Log(x))))) + 3
}

// primeSieve computes primes < n using a bit-packed sieve and returns
// both a set (map) for quick membership checks and a slice of primes.
func primeSieve(n int) []uint32 {
	var isPrime = bytes.Repeat([]byte{0b11111111}, int(math.Ceil(float64(n)/8.0)))
	for p := uint32(2); p*p < uint32(n); p++ {
		if (isPrime[p/8] & (1 << (7 - p%8))) != 0 {
			for i := p * p; i < uint32(n); i += p {
				isPrime[i/8] &= ^(byte(1) << (7 - i%8))
			}
		}
	}

	var primeSlice = make([]uint32, 0)
	for i, byte_ := range isPrime {
		if byte_ == 0 {
			continue
		}

		for bit := range 8 {
			bitmask := byte(1 << (7 - bit))
			if byte_&bitmask != 0 {
				var value = uint32(i*8 + bit)
				if value < 2 || value >= uint32(n) {
					continue
				}
				primeSlice = append(primeSlice, value)
			}
		}
	}

	return primeSlice
}

func writePrimesToFile(path string, primes []uint32) error {
	f, err := os.Create(path)
	if err != nil {
		return err
	}
	defer f.Close()

	w := bufio.NewWriter(f)
	if err := binary.Write(w, binary.LittleEndian, uint32(len(primes))); err != nil {
		return err
	}
	for _, p := range primes {
		if err := binary.Write(w, binary.LittleEndian, uint32(p)); err != nil {
			return err
		}
	}
	return w.Flush()
}

func main() {
	// n := math.MaxUint32
	n := 1_000_000
	if len(os.Args) > 1 {
		if v, err := strconv.Atoi(strings.TrimSpace(os.Args[1])); err == nil && v > 0 {
			n = v
		}
	}

	primes := primeSieve(n)
	if err := writePrimesToFile("Problem829/primes.bin", primes); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}

	fmt.Printf("Wrote %d primes to Problem829/primes.bin\n", len(primes))
}
