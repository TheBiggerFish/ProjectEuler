# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 85

# Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.


# ((W + 1) choose 2) + ((H + 1) choose 2)
def nearest_subrectangle_count(goal,max_):
    nearest = 0
    area = 0
    for m in range(1,max_):
        for n in range(m,max_):
            sub = m * (m+1) * n * (n+1) / 4
            if abs(goal - sub) < abs(goal - nearest):
                nearest = sub
                area = m * n
    print(nearest)
    return area

print(nearest_subrectangle_count(2*10**6,2000))