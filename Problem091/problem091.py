# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 91

# There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
    # 0 ≤ x1, y1, x2, y2 ≤ 2.
# Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?


from EulerLib.geometry import LineSegment, Point, Line, Triangle
import matplotlib.collections as mc
import matplotlib.pyplot as plt
import numpy as np

def how_many_right_triangles(bounds):
    count = 0
    O = Point(0,0)

    y = 0
    for x in range(1,bounds+1):
        for y in range(1,bounds+1):
            p1 = Point(x,y)
            ls = LineSegment(O,p1)
            other_leg = Line.extend_segment(ls).perpendicular(p1)
            points = other_leg.integer_points_along(lower_bound=Point(p1.x+1,0), upper_bound=Point(bounds,p1.y))
            count += len(points)*2

    count += 3*bounds**2 #To handle right angles at origin or on axis
    return count

print(how_many_right_triangles(50))