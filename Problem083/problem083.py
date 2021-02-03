# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 83

# Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt


from EulerLib.point import Point
from queue import PriorityQueue

with open('Problem083/matrix.txt') as f:
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
        if p1 not in prev and p1 not in seen and 0 <= p1.x <= target.x and 0 <= p1.y <= target.y:
            prev[p1] = cur
            q.put((get_g(p1,prev)+get_h(p1,target),p1))
            
        p2 = cur + Point(1,0)
        if p2 not in prev and p2 not in seen and 0 <= p2.x <= target.x and 0 <= p2.y <= target.y:
            prev[p2] = cur
            q.put((get_g(p2,prev)+get_h(p2,target),p2))

        p3 = cur + Point(0,-1)
        if p3 not in prev and p3 not in seen and 0 <= p3.x <= target.x and 0 <= p3.y <= target.y:
            prev[p3] = cur
            q.put((get_g(p3,prev)+get_h(p3,target),p3))

        p4 = cur + Point(-1,0)
        if p4 not in prev and p4 not in seen and 0 <= p4.x <= target.x and 0 <= p4.y <= target.y:
            prev[p4] = cur
            q.put((get_g(p4,prev)+get_h(p4,target),p4))

    return None

print(a_star(Point(0,0),Point(len(grid[0])-1,len(grid)-1)))