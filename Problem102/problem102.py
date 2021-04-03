# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 102

# Find the number of triangles for which the interior contains the origin.


from EulerLib.geometry import Point,Triangle,ORIGIN

with open('Problem102/triangles.txt') as f:
    count = 0
    for line in f:
        nums = [int(num) for num in line.strip().split(',')]
        t = Triangle(Point(nums[0],nums[1]),Point(nums[2],nums[3]),Point(nums[4],nums[5]))
        if ORIGIN in t:
            count += 1
    print(count)