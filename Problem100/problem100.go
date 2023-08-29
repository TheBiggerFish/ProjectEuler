package main

import (
	"fmt"
	"math"
)

type uint128 struct {
	upper uint64
	lower uint64
}

func (self uint128) add(other uint128) uint128 {
	new := uint128{
		self.upper + other.upper,
		self.lower + other.lower,
	}

	if new.lower < self.lower {
		new.upper += 1
	}

	return new
}

func (self uint128) sub(other uint128) uint128 {
	new := uint128{
		self.upper - other.upper,
		self.lower - other.lower,
	}

	if new.lower > self.lower {
		new.upper -= 1
	}

	return new
}

func (self uint128) lshift(bits int) uint128 {
	if bits < 0 || bits > 127 {
		return uint128{0, 0}
	}

	if bits > 64 {
		return uint128{
			self.lower << (bits - 64),
			0,
		}
	}

	mask := uint64(0xFFFF_FFFF_FFFF_FFFF) << (64 - bits)

	return uint128{
		(self.upper << bits) | ((self.lower & mask) >> (64 - bits)),
		self.lower << bits,
	}
}

func (self uint128) eq(other uint128) bool {
	return self.upper == other.upper && self.lower == other.lower
}

func (self uint128) gt(other uint128) bool {
	return self.upper > other.upper || (self.upper == other.upper && self.lower > other.lower)
}

func (self uint128) lt(other uint128) bool {
	return self.upper < other.upper || (self.upper == other.upper && self.lower < other.lower)
}

func (self uint128) mult(other uint128) uint128 {
	self_lower_low := (self.lower << 32) >> 32
	other_lower_low := (other.lower << 32) >> 32
	self_lower_high := self.lower >> 32
	other_lower_high := other.lower >> 32

	first_last := uint128{
		self_lower_high * other_lower_high,
		self_lower_low * other_lower_low,
	}
	outer_inner := (self_lower_high*other_lower_low + self_lower_low*other_lower_high)
	return first_last.add(uint128{
		outer_inner >> 32,
		outer_inner << 32,
	})
}

func main() {
	MIN := math.Pow(float64(10), float64(3))
	RATIO := math.Pow(0.5, 0.5)

	blue := uint128{0, uint64(RATIO * MIN)}
	red := uint128{0, uint64((1 - RATIO) * MIN)}

	var n, d, n2 uint128
	for true {
		n = blue.mult(blue.sub(uint128{0, 1}))
		n2 = n.lshift(1)
		d = (blue.add(red)).mult(blue.add(red).sub(uint128{0, 1}))

		if red.lower%100_000_000 == 0 || blue.lower%100_000_000 == 0 {
			fmt.Printf("%d,%d\n", blue.lower, red.lower)
		}

		if n2.lt(d) {
			blue = blue.add(uint128{0, 1})
		} else if n2.gt(d) {
			red = red.add(uint128{0, 1})
		} else {
			fmt.Printf("FOUND: %d, %d\n", blue.lower, red.lower)
			break
		}
	}
}
