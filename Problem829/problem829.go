package main

import (
	"bufio"
	"cmp"
	"encoding/binary"
	"fmt"
	"math"
	"os"
	"slices"
	"sort"

	bin "math/bits"
)

// The number of primes loaded into PRIME_SET and PRIME_SLICE
var PRIME_MAX uint64 = 1_000_000

// The max number n to precompute for KNOWN_VALUES
var MAX_PRECOMP_TREE int = 1_000_000

// PRIME_SET is a hash set of the first PRIME_MAX prime numbers
var PRIME_SET map[uint64]struct{}

// PRIME_SLICE is a slice of the first PRIME_MAX prime numbers in ascending order
var PRIME_SLICE []uint64

// SOLVE represents known solutions to the problem which are used for answer-checking
var SOLVE = []uint64{0, 0, 2, 2, 8, 4, 32, 8, 256, 72, 3456, 540, 20480, 1800, 276480, 512, 10321920, 36000, 185794560, 306180, 3236954112, 2700000, 81749606400, 2160000, 1961990553600, 6998400, 51011754393600, 293932800, 1428329123020800, 1233357840000, 40260046159872000, 26129782224000}

// KNOWN_VALUES is the mapping from tree-encoding e to the numbers n where T(n) would be encoded as e
var KNOWN_VALUES = make(map[uint64][]uint64)

// Loads precomputed primes from a binary file
func loadPrimes(primeMax uint64) (map[uint64]struct{}, []uint64) {
	// Try reading a precomputed primes file written by `writePrimesToFile`.
	f, err := os.Open("Problem829/primes.bin")
	if err == nil {
		defer f.Close()
		r := bufio.NewReader(f)
		var count32 uint32
		if err := binary.Read(r, binary.LittleEndian, &count32); err == nil {
			count := uint64(count32)
			primes := make([]uint64, 0, count)
			for i := uint64(0); i < count; i++ {
				var p uint32
				if err := binary.Read(r, binary.LittleEndian, &p); err != nil {
					primes = nil
					break
				}
				primes = append(primes, uint64(p))
				if primeMax > 0 && uint64(p) >= primeMax {
					primeMax = uint64(p)
					break
				}
			}
			if primes != nil {
				set := make(map[uint64]struct{}, len(primes))
				for _, p := range primes {
					set[p] = struct{}{}
				}
				PRIME_MAX = primes[len(primes)-1]
				return set, primes
			}
		}
	}
	panic("failed to load primes")
}

// precomputeTrees generates KNOWN_VALUES for composite numbers up to a value of MAX_PRECOMP_TREE
func precomputeTrees(maxPrecompTree int) map[uint64][]uint64 {
	knownValues := make(map[uint64][]uint64)
	for i := 2; i < maxPrecompTree; i++ {
		if _, ok := PRIME_SET[uint64(i)]; ok {
			continue
		}
		factors := primeFactorize(uint64(i))
		tree := &BinaryTree{}
		T(factors, tree, 0)
		encoding := tree.GetSubTreeShapeEncoding(0)
		if encoding != 0 {
			knownValues[encoding] = append(knownValues[encoding], uint64(i))
		}
	}
	return knownValues
}

// BinaryTree is a simple heap-indexed binary tree. Nodes are stored in
// level-order in the `Values` slice: root at index 0, left child at
// 2*i+1 and right child at 2*i+2.
type BinaryTree struct {
	Values []uint64
}

// SetNode sets the value at nodeId, growing the internal slice if needed.
func (tree *BinaryTree) SetNode(nodeId int, value uint64) {
	if nodeId >= len(tree.Values) {
		tree.Values = append(tree.Values, slices.Repeat([]uint64{0}, nodeId-len(tree.Values)+1)...)
	}
	tree.Values[nodeId] = value
}

// GetNode fetches the value stored at the given node id, defaulting to 0 if out of bounds
func (tree *BinaryTree) GetNode(node int) uint64 {
	if node < 0 || node >= len(tree.Values) {
		return 0
	}
	return tree.Values[node]
}

// getStructureTreeHelper is the recursive helper function GetStructureTree()
func (tree *BinaryTree) getStructureTreeHelper(node int, structureTree *BinaryTree) uint64 {
	if node >= len(tree.Values) || tree.Values[node] == 0 {
		return uint64(0)
	}
	l := tree.getStructureTreeHelper(node*2+1, structureTree)
	r := tree.getStructureTreeHelper(node*2+2, structureTree)

	var value uint64
	if l == 0 && r == 0 {
		value = 1
	} else {
		value = l + r
	}
	structureTree.Values[node] = value
	return value
}

// GetStructureTree returns the "structure tree" for the current tree.
// The structure tree is a tree with the same shape, but the value of
// every node reflects the number of leaf nodes below on the tree.
func (tree *BinaryTree) GetStructureTree() BinaryTree {
	result := BinaryTree{Values: make([]uint64, len(tree.Values))}
	tree.getStructureTreeHelper(0, &result)
	return result
}

// getSubTreeShapeEncodingHelper is the recursive helper function for GetSubTreeShapeEncoding()
func (tree *BinaryTree) getSubTreeShapeEncodingHelper(originNode, destNode int, shapeSlice *uint64) error {
	if originNode >= len(tree.Values) || tree.Values[originNode] == 0 || destNode >= 64 {
		return fmt.Errorf("node out of bounds or empty")
	}

	*shapeSlice |= 1 << destNode
	tree.getSubTreeShapeEncodingHelper(originNode*2+1, destNode*2+1, shapeSlice)
	tree.getSubTreeShapeEncodingHelper(originNode*2+2, destNode*2+2, shapeSlice)
	return nil
}

// GetSubTreeShapeEncoding returns the shape encoding for the subtree rooted at the given node.
// A shape encoding is a bitmap which reflects the structure of the subtree.
func (tree *BinaryTree) GetSubTreeShapeEncoding(node int) uint64 {
	var shape uint64
	err := tree.getSubTreeShapeEncodingHelper(node, 0, &shape)
	if err != nil {
		return 0
	}
	return shape
}

// buildSmallestTwinTreeHelper is the recursive helper function for BuildSmallestTwinTree()
func (tree *BinaryTree) buildSmallestTwinTreeHelper(twinTree *BinaryTree, structureTree BinaryTree, node int, minValue uint64) uint64 {
	// leafCount represents the number of leaves below the current node (thus the number of prime factors of this node in the tree)
	leafCount := structureTree.GetNode(node)
	if leafCount == 0 {
		// Should never reach this
		return 0
	}

	// if this node has only one prime factor, then it is itself prime and we can look for its value in the precomputed PRIME_SET
	if leafCount == 1 {
		if _, ok := PRIME_SET[minValue]; !ok {
			fmt.Printf("Provided minValue is not a valid prime: %d\n", minValue)
		}
		twinTree.Values[node] = minValue
		return minValue
	}

	// minValue must be at least 2 ^ (#factors)
	minPow2 := uint64(math.Pow(2, float64(leafCount)))
	if minValue < minPow2 {
		minValue = minPow2
	}

	// determine the bitmap for the original tree
	targetEncoding := tree.GetSubTreeShapeEncoding(node)
	if len(KNOWN_VALUES[targetEncoding]) != 0 {
		// if known values exist for this shape, grab the lowest which is greater than minValue
		var bestValue uint64 = 0
		for _, val := range KNOWN_VALUES[targetEncoding] {
			if val >= minValue {
				bestValue = val
				break
			}
		}
		// take the bestValue and fill out the tree with it
		if bestValue > 0 {
			T(primeFactorize(bestValue), twinTree, node)
			return bestValue
		}
	}

	var l, r uint64
	var candidateNodeValue uint64
	var maxL uint64 = math.MaxUint64
	var bestValue, bestL, bestR uint64 = math.MaxUint64, 0, 0
	var minL uint64 = uint64(0.75 * math.Sqrt(float64(minValue))) // could theoretically miss optimal choice, but unlikely.

	// Loop until we find a candidate value, then continue until we're sure there's no better candidate
	for candidateNodeValue == 0 || l < maxL {
		l = tree.buildSmallestTwinTreeHelper(twinTree, structureTree, node*2+1, minL)

		// r can be no less than max(l, minValue/l)
		var minR uint64 = l
		if minR*l < minValue {
			minR = uint64(math.Ceil(float64(minValue) / float64(l)))
		}
		r = tree.buildSmallestTwinTreeHelper(twinTree, structureTree, node*2+2, minR)

		// step forward minL for the next try (if required)
		minL = l + 1

		// check that the proposed tree has the correct shape
		var testTree BinaryTree
		factors := append(primeFactorize(l), primeFactorize(r)...)
		T(factors, &testTree, 0)
		if targetEncoding == testTree.GetSubTreeShapeEncoding(0) {
			if maxL > r {
				// once we have a good candidate, stop looking when maxL reaches the lowest valid value of r which has given us a candidate
				maxL = r
			}
			candidateNodeValue = l * r
			if candidateNodeValue < bestValue {
				// we're looking for minimal candidate
				bestValue = candidateNodeValue
				bestL = l
				bestR = r
			}
		}
	}

	// check if optimal subtrees have been overwritten and repopulate
	if tree.GetNode(node*2+1) != bestL {
		l = tree.buildSmallestTwinTreeHelper(twinTree, structureTree, node*2+1, bestL)
	}
	if tree.GetNode(node*2+2) != bestR {
		r = tree.buildSmallestTwinTreeHelper(twinTree, structureTree, node*2+2, bestR)
	}

	// set node to correct value
	twinTree.SetNode(node, bestValue)
	return bestValue
}

// BuildSmallestTwinTree recursively searches for the tree with the same shape as the original with minimal value.
func (tree *BinaryTree) BuildSmallestTwinTree() BinaryTree {
	result := BinaryTree{Values: make([]uint64, len(tree.Values))}
	tree.buildSmallestTwinTreeHelper(&result, tree.GetStructureTree(), 0, 2)
	return result
}

// prod returns the product of elements
func prod(nums []uint64) uint64 {
	var p uint64 = 1
	for _, n := range nums {
		p *= n
	}
	return p
}

// powerSet returns all subsets of numbers whose size is <= r. Results
// are deduplicated and returned as a slice of slices.
func powerSet(numbers []uint64, r int) [][]uint64 {
	var results [][]uint64

	bits := uint64(len(numbers))
	max := uint64(1) << bits
	for i := range max {
		count := bin.OnesCount64(i)
		if count > r {
			continue
		}

		result := make([]uint64, 0, bits)

		for bit := bits; bit > 0; bit-- {
			shifted := uint64(1 << (bit - 1))
			if i&shifted != 0 {
				result = append(result, numbers[bit-1])
			}
		}

		results = append(results, result)
	}
	slices.SortFunc(results, slices.Compare)
	results = slices.CompactFunc(results, slices.Equal)
	return results
}

// primeFactorize returns the prime factors of n
func primeFactorize(n uint64) []uint64 {
	var factors []uint64
	for _, p := range PRIME_SLICE {
		if p*p > n {
			break
		}
		for n%p == 0 {
			factors = append(factors, p)
			n /= p
		}
	}

	if n > PRIME_MAX*PRIME_MAX {
		panic(fmt.Sprint("Number too large to assert primeness: %ud", n))
	} else if n > 1 {
		factors = append(factors, n)
	}
	slices.Sort(factors)
	return factors
}

// primeFactorizeFactorial returns the prime factors of n!! as a sorted slice
func primeFactorizeFactorial(n uint64) []uint64 {
	var primeFactors []uint64

	for i := n; i > 1; i -= 2 {
		for _, p := range primeFactorize(i) {
			primeFactors = append(primeFactors, p)
		}
	}
	slices.Sort(primeFactors)
	return primeFactors
}

// partition splits factors into two slices whose products are as close as possible
func partition(factors []uint64) ([]uint64, []uint64) {
	var target float64
	for _, f := range factors {
		target += math.Log(float64(f))
	}
	target /= 2
	var split = len(factors) / 2
	var left, right = factors[:split], factors[split:]

	type factorSet struct {
		value float64
		set   []uint64
	}

	var rightSet []factorSet
	for _, set := range powerSet(right, len(right)) {
		var value float64
		for _, f := range set {
			value += math.Log(float64(f))
		}
		rightSet = append(rightSet, factorSet{value: value, set: set})
	}
	sort.Slice(rightSet, func(i, j int) bool {
		return rightSet[i].value < rightSet[j].value
	})

	var bestLeft, bestRight []uint64
	var bestDistance float64 = math.Inf(1)

	for _, set := range powerSet(left, len(left)) {
		var value float64
		for _, f := range set {
			value += math.Log(float64(f))
		}
		var offset = target - value
		i, _ := slices.BinarySearchFunc(rightSet, offset, func(f factorSet, target float64) int {
			return cmp.Compare(f.value, target)
		})
		var closest factorSet
		if i == 0 {
			closest = rightSet[0]
		} else if i == len(rightSet) {
			closest = rightSet[i-1]
		} else {
			candidate1, candidate2 := rightSet[i-1], rightSet[i]
			if math.Abs(candidate1.value-offset) < math.Abs(candidate2.value-offset) {
				closest = candidate1
			} else {
				closest = candidate2
			}
		}
		var distance = math.Abs(closest.value - offset)
		if distance < bestDistance {
			bestDistance = distance
			bestLeft, bestRight = set, closest.set
		}
	}

	part1 := append(bestLeft, bestRight...)
	slices.Sort(part1)

	freq := make(map[uint64]int)
	for _, f := range factors {
		freq[f]++
	}
	for _, f := range part1 {
		freq[f]--
	}

	part2 := make([]uint64, 0)
	for f, count := range freq {
		for range count {
			part2 = append(part2, f)
		}
	}
	slices.Sort(part2)

	if prod(part1) > prod(part2) {
		part1, part2 = part2, part1
	}

	return part1, part2
}

// T builds the binary tree of factors where each pair of children is as close as possible
func T(factors []uint64, tree *BinaryTree, nodeId int) {
	if tree == nil {
		panic("Tree is nil")
	} else if len(factors) == 0 {
		return
	}

	tree.SetNode(nodeId, prod(factors))
	if len(factors) <= 1 {
		return
	}
	left, right := partition(factors)
	T(left, tree, nodeId*2+1)
	T(right, tree, nodeId*2+2)
}

// M returns the smallest number that has a factor tree identical in shape to the factor tree for n!!
func M(min, max, step int) uint64 {
	var sum uint64
	for i := min; i <= max; i += step {
		baseFactors := primeFactorizeFactorial(uint64(i))
		tree := &BinaryTree{}
		T(baseFactors, tree, 0)

		twinTree := tree.BuildSmallestTwinTree()
		// fmt.Println(strings.Join(strings.Fields(fmt.Sprint(tree.Values)), ","))
		// fmt.Println(strings.Join(strings.Fields(fmt.Sprint(twinTree.Values)), ","))
		var bonus string
		if i < len(SOLVE) && twinTree.GetNode(0) != SOLVE[i] {
			bonus = " (WRONG)"
		}
		fmt.Printf("M(%d) = %d%s\n", i, twinTree.GetNode(0), bonus)
		sum += twinTree.GetNode(0)
	}
	return sum
}

func main() {
	PRIME_SET, PRIME_SLICE = loadPrimes(PRIME_MAX)
	KNOWN_VALUES = precomputeTrees(MAX_PRECOMP_TREE)

	fmt.Printf("Solution: %d\n", M(2, 31, 1))
}
