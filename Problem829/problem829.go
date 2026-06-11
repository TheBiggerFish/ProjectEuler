package main

import (
	"bufio"
	"cmp"
	"encoding/binary"
	"flag"
	"fmt"
	"math"
	"os"
	"runtime/pprof"
	"slices"
	"sort"
	"strings"

	bin "math/bits"
)

var PRIME_MAX uint64 = 10_000_000
var MAX_PRECOMP_TREE int = 1_000_000
var PRIME_SET map[uint64]struct{}
var PRIME_SLICE []uint64
var SOLVE = []uint64{0, 0, 2, 2, 8, 4, 32, 8, 256, 72, 3456, 540, 20480, 1800, 276480, 512, 10321920, 36000, 185794560, 306180, 3236954112, 2700000, 81749606400, 2160000, 1961990553600, 6998400, 51011754393600, 293932800, 1428329123020800, 1233357840000, 40260046159872000, 26129782224000}
var SOLVE_TREE BinaryTree
var KNOWN_VALUES = make(map[uint64][]uint64)
var KNOWN_TREES = make(map[uint64]uint64)

func loadPrimes() (map[uint64]struct{}, []uint64) {
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
				if PRIME_MAX > 0 && uint64(p) >= PRIME_MAX {
					PRIME_MAX = uint64(p)
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

func precomputeTrees() {
	for i := 2; i < MAX_PRECOMP_TREE; i++ {
		if _, ok := PRIME_SET[uint64(i)]; ok {
			continue
		}
		factors := primeFactorize(uint64(i))
		tree := &BinaryTree{}
		T(factors, tree, 0)
		encoding := tree.GetSubTreeShapeEncoding(0)
		if encoding != 0 {
			KNOWN_VALUES[encoding] = append(KNOWN_VALUES[encoding], uint64(i))
			KNOWN_TREES[uint64(i)] = encoding
		}
	}
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

func (tree *BinaryTree) LeftChild(parentNode int) int {
	return parentNode*2 + 1
}

func (tree *BinaryTree) RightChild(parentNode int) int {
	return parentNode*2 + 2
}

// InsertLeftChild inserts value as the left child of parentNode.
func (tree *BinaryTree) InsertLeftChild(parentNode int, value uint64) {
	tree.SetNode(tree.LeftChild(parentNode), value)
}

// InsertRightChild inserts value as the right child of parentNode.
func (tree *BinaryTree) InsertRightChild(parentNode int, value uint64) {
	tree.SetNode(tree.RightChild(parentNode), value)
}

func (tree *BinaryTree) GetNode(node int) uint64 {
	if node < 0 || node >= len(tree.Values) {
		return 0
	}
	return tree.Values[node]
}

func (tree *BinaryTree) GetLeftChild(parentNode int) uint64 {
	return tree.GetNode(tree.LeftChild(parentNode))
}

func (tree *BinaryTree) GetRightChild(parentNode int) uint64 {
	return tree.GetNode(tree.RightChild(parentNode))
}

func (tree *BinaryTree) HasSameShape(other *BinaryTree) bool {
	if len(tree.Values) != len(other.Values) {
		return false
	}
	for i := range len(tree.Values) {
		if tree.Values[i] == 0 && other.Values[i] != 0 {
			return false
		}
		if tree.Values[i] != 0 && other.Values[i] == 0 {
			return false
		}
	}
	return true
}

func (tree *BinaryTree) getSubTreeHelper(originNode, destNode int, subTree *BinaryTree) {
	if originNode >= len(tree.Values) || tree.Values[originNode] == 0 {
		return
	}
	subTree.SetNode(destNode, tree.GetNode(originNode))
	tree.getSubTreeHelper(originNode*2+1, destNode*2+1, subTree)
	tree.getSubTreeHelper(originNode*2+2, destNode*2+2, subTree)
}

func (tree *BinaryTree) GetSubTree(node int) BinaryTree {
	subTree := BinaryTree{Values: make([]uint64, 0, len(tree.Values))}
	tree.getSubTreeHelper(node, 0, &subTree)
	return subTree
}

func (tree *BinaryTree) insertSubTreeHelper(originNode, destNode int, subTree *BinaryTree) {
	if originNode >= len(subTree.Values) && destNode >= len(tree.Values) {
		return
	} else if originNode >= len(subTree.Values) || destNode >= len(tree.Values) {
	} else if subTree.Values[originNode] == 0 && tree.Values[destNode] == 0 {
		return
	}
	tree.SetNode(destNode, subTree.GetNode(originNode))
	tree.insertSubTreeHelper(originNode*2+1, destNode*2+1, subTree)
	tree.insertSubTreeHelper(originNode*2+2, destNode*2+2, subTree)
}

func (tree *BinaryTree) InsertSubTree(node int, subTree BinaryTree) {
	tree.insertSubTreeHelper(0, node, &subTree)
	var i int
	for i = len(tree.Values) - 1; i > 0; i-- {
		if tree.Values[i] != 0 {
			break
		}
	}
	tree.Values = tree.Values[:i+1]
}

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

func (tree *BinaryTree) GetStructureTree() BinaryTree {
	result := BinaryTree{Values: make([]uint64, len(tree.Values))}
	tree.getStructureTreeHelper(0, &result)
	return result
}

func (tree *BinaryTree) getSubTreeShapeEncodingHelper(originNode, destNode int, shapeSlice *uint64) error {
	if originNode >= len(tree.Values) || tree.Values[originNode] == 0 || destNode >= 64 {
		return fmt.Errorf("node out of bounds or empty")
	}

	*shapeSlice |= 1 << destNode
	tree.getSubTreeShapeEncodingHelper(originNode*2+1, destNode*2+1, shapeSlice)
	tree.getSubTreeShapeEncodingHelper(originNode*2+2, destNode*2+2, shapeSlice)
	return nil
}

func (tree *BinaryTree) GetSubTreeShapeEncoding(node int) uint64 {
	var shape uint64
	err := tree.getSubTreeShapeEncodingHelper(node, 0, &shape)
	if err != nil {
		return 0
	}
	return shape
}

func (tree *BinaryTree) buildSmallestTwinTreeHelper(twinTree *BinaryTree, structureTree BinaryTree, node int, minValue uint64) uint64 {
	leafCount := structureTree.GetNode(node)
	if leafCount == 0 {
		return 0
	}

	if leafCount == 1 {
		var minPrime uint64
		if _, ok := PRIME_SET[minValue]; ok {
			minPrime = minValue
		} else {
			for _, minPrime = range PRIME_SLICE {
				if minPrime >= minValue {
					break
				}
			}
		}
		twinTree.Values[node] = minPrime
		return minPrime
	}

	minPow2 := uint64(math.Pow(2, float64(leafCount)))
	if minValue < minPow2 {
		minValue = minPow2
	}

	targetEncoding := tree.GetSubTreeShapeEncoding(node)
	if len(KNOWN_VALUES[targetEncoding]) != 0 {
		var bestValue uint64 = 0
		for _, val := range KNOWN_VALUES[targetEncoding] {
			if val >= minValue {
				bestValue = val
				break
			}
		}
		if bestValue > 0 {
			T(primeFactorize(bestValue), twinTree, node)
			return bestValue
		}
	}

	var l, r uint64
	var nodeVal uint64
	var minL uint64 = uint64(0.75 * math.Sqrt(float64(minValue)))
	var maxL uint64 = math.MaxUint64
	var minR uint64 = minL
	var bestValue, bestL, bestR uint64 = math.MaxUint64, 0, 0
	for nodeVal == 0 || l < maxL {
		if l >= 900_000 {
			print()
		}
		l = tree.buildSmallestTwinTreeHelper(twinTree, structureTree, node*2+1, minL)
		minR = l
		if minR*l < minValue {
			minR = uint64(math.Ceil(float64(minValue) / float64(l)))
		}
		r = tree.buildSmallestTwinTreeHelper(twinTree, structureTree, node*2+2, minR)

		minL = l + 1
		var testTree BinaryTree
		factors := append(primeFactorize(l), primeFactorize(r)...)
		T(factors, &testTree, 0)
		if targetEncoding == testTree.GetSubTreeShapeEncoding(0) {
			if maxL > r {
				maxL = r
			}
			nodeVal = l * r
			if nodeVal < bestValue {
				bestValue = nodeVal
				bestL = l
				bestR = r
			}
		}
	}

	l = tree.buildSmallestTwinTreeHelper(twinTree, structureTree, node*2+1, bestL)
	r = tree.buildSmallestTwinTreeHelper(twinTree, structureTree, node*2+2, bestR)
	twinTree.SetNode(node, bestValue)
	return bestValue

	// var leftEncoding = tree.GetSubTreeShapeEncoding(tree.LeftChild(node))
	// var rightEncoding = tree.GetSubTreeShapeEncoding(tree.RightChild(node))

	// var target uint64
	// var currentMin uint64 = math.MaxUint32
	// var bestR uint64 = math.MaxUint32
	// lCache, rCache := make(map[uint64]uint64), make(map[uint64]uint64)
	// for target = minValue; target <= currentMin; target++ {
	// 	if _, ok := PRIME_SET[target]; ok {
	// 		continue
	// 	}
	// 	if target < uint64(MAX_PRECOMP_TREE) && targetEncoding != KNOWN_TREES[target] {
	// 		continue
	// 	}

	// 	factors := primeFactorize(target)
	// 	if len(factors) != int(leafCount) {
	// 		continue
	// 	}
	// 	if target < uint64(MAX_PRECOMP_TREE) {
	// 		T(factors, twinTree, node)
	// 		return target
	// 	}

	// 	left, right := partition(factors)
	// 	if uint64(len(left)) != lLeaf {
	// 		continue
	// 	}
	// 	l, r := prod(left), prod(right)
	// 	if l > bestR {
	// 		bestR = math.MaxUint64
	// 	} else if r > bestR {
	// 		continue
	// 	}

	// 	var actualL uint64
	// 	if cachedL, ok := lCache[l]; ok {
	// 		actualL = cachedL
	// 	} else {
	// 		subTree := tree.GetSubTree(node*2 + 1)
	// 		actualL = subTree.buildSmallestTwinTreeHelper(&subTree, subTree.GetStructureTree(), 0, l)
	// 		for i := l; i <= actualL; i++ {
	// 			if _, ok := lCache[i]; ok {
	// 				break
	// 			}
	// 			lCache[i] = actualL
	// 		}
	// 	}

	// 	if actualL != l {
	// 		continue
	// 	}

	// 	var actualR uint64
	// 	if cachedR, ok := rCache[r]; ok {
	// 		actualR = cachedR
	// 	} else {
	// 		subTree := tree.GetSubTree(node*2 + 2)
	// 		actualR = subTree.buildSmallestTwinTreeHelper(&subTree, subTree.GetStructureTree(), 0, r)
	// 		for i := r; i <= actualR; i++ {
	// 			rCache[i] = actualR
	// 		}
	// 		if actualR < bestR {
	// 			bestR = actualR
	// 		}
	// 	}

	// 	if actualR != r {
	// 		continue
	// 	}

	// 	tree.buildSmallestTwinTreeHelper(twinTree, structureTree, node*2+1, actualL)
	// 	tree.buildSmallestTwinTreeHelper(twinTree, structureTree, node*2+2, actualR)
	// 	twinTree.SetNode(node, target)
	// 	return target

	// }

	return 0
}

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

// primeFactorizeFactorial returns the concatenated prime factors of n!! sorted
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

func M(min, max, step int) uint64 {

	var sum uint64
	// i := n
	for i := min; i <= max; i += step {
		// fmt.Println(i)

		T(primeFactorize(SOLVE[i]), &SOLVE_TREE, 0)
		baseFactors := primeFactorizeFactorial(uint64(i))
		tree := &BinaryTree{}
		T(baseFactors, tree, 0)

		// structureTree := tree.GetStructureTree()
		twinTree := tree.BuildSmallestTwinTree()
		fmt.Println(strings.Join(strings.Fields(fmt.Sprint(tree.Values)), ","))
		// fmt.Println(strings.Join(strings.Fields(fmt.Sprint(structureTree.Values)), ","))
		fmt.Println(strings.Join(strings.Fields(fmt.Sprint(twinTree.Values)), ","))
		var bonus string
		if i < len(SOLVE) && twinTree.GetNode(0) != SOLVE[i] {
			bonus = " (WRONG)"
		}
		fmt.Printf("M(%d) = %d%s\n", i, twinTree.GetNode(0), bonus)
		sum += twinTree.GetNode(0)
	}
	return uint64(sum)
}

func main() {
	cpuProfile := flag.String("cpuprofile", "", "write cpu profile to file")
	flag.Parse()

	PRIME_SET, PRIME_SLICE = loadPrimes()
	precomputeTrees()

	solve := func() {
		M(2, 31, 1)
	}

	if *cpuProfile != "" {
		f, err := os.Create(*cpuProfile)
		if err != nil {
			panic(err)
		}
		if err := pprof.StartCPUProfile(f); err != nil {
			panic(err)
		}
		solve()
		pprof.StopCPUProfile()
		if err := f.Close(); err != nil {
			panic(err)
		}
		return
	}

	// tree := &BinaryTree{}
	// // // T(primeFactorizeFactorial(21), tree, 0)
	// T(primeFactorize(SOLVE[19]), tree, 0)
	// fmt.Println(strings.Join(strings.Fields(fmt.Sprint(tree.Values)), ","))

	solve()

	// structureTree := tree.GetStructureTree()
	// twinTree := tree.BuildSmallestTwinTree()
	// // subTree := tree.GetSubTree(2)
	// // tree.InsertSubTree(1, subTree)
	// fmt.Println(strings.Join(strings.Fields(fmt.Sprint(structureTree.Values)), ","))
	// fmt.Println(strings.Join(strings.Fields(fmt.Sprint(twinTree.Values)), ","))
	// fmt.Println(strings.Join(strings.Fields(fmt.Sprint(subTree.Values)), ","))

	// print(strings.Join(strings.Fields(fmt.Sprint(primeFactorize(783))), ","))
	// p1, p2 := partition(primeFactorize(992))
	// print(strings.Join(strings.Fields(fmt.Sprint(p1)), ","))
	// print(strings.Join(strings.Fields(fmt.Sprint(p2)), ","))
	// numbers := []uint64{1, 1, 2, 3}
	// r := 3
	// fmt.Println(len(powerSet(numbers, r)))
}
