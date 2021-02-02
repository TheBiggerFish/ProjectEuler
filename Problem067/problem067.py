# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 67

# Find the maximum total from top to bottom in triangle.txt, a 15K text file containing a triangle with one-hundred rows.


def read(filename):
    with open(filename) as f:
        return [[int(item) for item in row.strip().split(' ')] for row in f]

def find_max_path(triangle):
    for row in reversed(range(len(triangle)-1)):
        for col in range(row+1):
            l = triangle[row+1][col]
            r = triangle[row+1][col+1]
            triangle[row][col] += max(l,r)
    return triangle[0][0]

print(find_max_path(read('Problem67/triangle.txt')))