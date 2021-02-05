# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 67

# Find the maximum total from top to bottom in triangle.txt, a 15K text file containing a triangle with one-hundred rows.
# https://en.wikipedia.org/wiki/A*_search_algorithm


from EulerLib.geometry import Point
from queue import PriorityQueue

with open('Problem067/triangle.txt') as f:
    grid = [[int(item) for item in row.strip().split(' ')] for row in f]
prev = {}

def get_h(pt):
    return (4-pt.y) * 10 - 1

def get_g(pt):
    return sum([grid[pt.y][pt.x] for pt in get_path(pt)])

def get_path(pt):
    path = [pt]
    while pt in prev:
        pt = prev[pt]
        path.append(pt)
    return path

def print_path(path):
    for pt in path:
        print(str(pt),'->',grid[pt.y][pt.x])

def a_star(start):
    q = PriorityQueue()
    q.put((0,start))
    seen = set()
    while not q.empty():
        cur = q.get()[1]
        if cur in seen:
            continue
        seen.add(cur)

        # print(cur)
        if cur.y == 4:
            return print_path(get_path(prev[cur]))
            
        g = get_g(cur)

        p1 = Point(cur.x,cur.y+1)
        prev[p1] = cur
        q.put((-g-get_h(p1),p1))

        p2 = Point(cur.x+1,cur.y+1)
        prev[p2] = cur
        q.put((-g-get_h(p2),p2))
    return None

print(a_star(Point(0,0)))

