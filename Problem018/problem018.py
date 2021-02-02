# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 18

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, find the maximum total from top to bottom of the triangle below:


tri = [[75],
        [95,64],
        [17,47,82],
        [18,35,87,10],
        [20,4,82,47,65],
        [19,1,23,75,3,34],
        [88,2,77,73,7,63,67],
        [99,65,4,28,6,16,70,92],
        [41,41,26,56,83,40,80,70,33],
        [41,48,72,33,47,32,37,16,94,29],
        [53,71,44,65,25,43,91,52,97,51,14],
        [70,11,33,28,77,73,17,78,39,68,17,57],
        [91,71,52,38,17,14,91,43,58,50,27,29,48],
        [63,66,4,68,89,53,67,30,73,16,69,87,40,31],
        [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

# Build a list of all binary numbers of length dim where dim is the width/height of the triangle
# Use the list to follow every possible path through the triangle
def max_path(tri):
    dim = len(tri)
    paths = []
    values = []
    for i in range(2**dim):
        string = "{0:b}".format(i).rjust(dim,'0')
        paths += [string]

    for path in paths:
        col = 0
        row = 0
        sum_ = 0
        for step in path:
            sum_ += tri[col][row]
            col += 1
            if step == '1':
                row += 1
        values.append(sum_)
    return max(values)

print(max_path(tri))