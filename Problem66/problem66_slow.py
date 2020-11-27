# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 66

# Consider quadratic Diophantine equations of the form: x^2 – Dy^2 = 1
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.


def find_y(x,D):
    return ((x**2 - 1) / D) ** 0.5

def diophantine(max_D,max_x):
    best_x = 2
    best_D = -1
    for D in range(2,max_D):
        if (D ** 0.5).is_integer():
            continue
        found = False
        for x in range(2 if D % 2 == 1 else 3,max_x, 1 if D % 2 == 1 else 2):
            if not (x % 2 == 1 or D % 2 == 1):
                continue
            y = find_y(x,D)
            if y.is_integer():
                print(x,D,y)
                # if D % 10 == 0:
                #     # print("Working")
                if x > best_x:
                    # print("BEST:",x,D,y)
                    best_x = x
                    best_D = D
                found = True
                break
        if not found:
            print("No x found for",D)
    return best_D

print(diophantine(1000,10000000))
