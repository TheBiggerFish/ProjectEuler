# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 82

# Find the minimal path sum from the left column to the right column in matrix.txt


from EulerLib.point import Point
from queue import PriorityQueue

with open('Problem082/matrix.txt') as f:
    grid = [[int(item) for item in row.strip().split(',')] for row in f]

def get_value(pt):
    return grid[pt.y][pt.x]

def get_h(pt,target_col):
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

def a_star(start,upper_bound):
    q = PriorityQueue()
    q.put((get_value(start),start))
    seen = set()
    prev = {}
    while not q.empty():
        cur = q.get()[1]
        if cur in seen:
            continue
        seen.add(cur)

        if cur.x == upper_bound.x:
            return get_g(cur,prev)

        p1 = cur + Point(0,1)
        if p1 not in prev and p1 not in seen and 0 <= p1.x <= upper_bound.x and 0 <= p1.y <= upper_bound.y:
            prev[p1] = cur
            q.put((get_g(p1,prev)+get_h(p1,upper_bound.x),p1))

        p2 = cur + Point(1,0)
        if p2 not in prev and p2 not in seen and 0 <= p2.x <= upper_bound.x and 0 <= p2.y <= upper_bound.y:
            prev[p2] = cur
            q.put((get_g(p2,prev)+get_h(p2,upper_bound.x),p2))
        
        p3 = cur + Point(0,-1)
        if p3 not in prev and p3 not in seen and 0 <= p3.x <= upper_bound.x and 0 <= p3.y <= upper_bound.y:
            prev[p3] = cur
            q.put((get_g(p3,prev)+get_h(p3,upper_bound.x),p3))
    return None

def min_a_star():
    min_ = 9999*len(grid)
    upper_bound = Point(len(grid)-1,len(grid)-1)
    for i in range(len(grid)):
        start = Point(0,i)
        min_ = min(min_,a_star(start,upper_bound))
    return min_

print(min_a_star())