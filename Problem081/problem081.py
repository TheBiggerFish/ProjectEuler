# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 81

# Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt


from EulerLib.geometry import Point
from queue import PriorityQueue

with open('Problem081/matrix.txt') as f:
    grid = [[int(item) for item in row.strip().split(',')] for row in f]

def get_value(pt):
    return grid[pt.y][pt.x]

def get_h(pt,target):
    return 0

def get_g(pt,prev):
    return sum([get_value(pt) for pt in get_path(pt,prev)])

def get_path(pt,prev):
    path = [pt]
    while pt in prev:
        pt = prev[pt]
        path.append(pt)
    return path

def print_path(path):
    for pt in path:
        print(str(pt),'->',get_value(pt))

def a_star(start,target):
    q = PriorityQueue()
    q.put((get_value(start),start))
    seen = set()
    prev = {}
    while not q.empty():
        cur = q.get()[1]
        if cur in seen:
            continue
        seen.add(cur)

        if cur == target:
            return get_g(cur,prev)

        p1 = cur + Point(0,1)
        if p1 not in prev and 0 <= p1.x <= target.x and 0 <= p1.y <= target.y:
            prev[p1] = cur
            q.put((get_g(p1,prev)+get_h(p1,target),p1))

        p2 = cur + Point(1,0)
        if p2 not in prev and 0 <= p2.x <= target.x and 0 <= p2.y <= target.y:
            prev[p2] = cur
            q.put((get_g(p2,prev)+get_h(p2,target),p2))
    return None

print(a_star(Point(0,0),Point(len(grid[0])-1,len(grid)-1)))