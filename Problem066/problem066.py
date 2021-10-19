# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 66

# Consider quadratic Diophantine equations of the form: x^2 – Dy^2 = 1
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
# https://en.wikipedia.org/wiki/Diophantine_equation
# https://en.wikipedia.org/wiki/Pell%27s_equation


from fishpy.fraction import ContinuedFraction


def pell_solution(D):
    if (D**0.5).is_integer():
        return -1
    h,k = 0,0
    i = 1
    while h**2 - (D * (k**2)) != 1:
        seq = ContinuedFraction.gen_sqrt_seq(D,i)
        con_frac = ContinuedFraction.gen_from_seq(seq)
        frac = con_frac.reduce_fraction()
        h,k = frac.n,frac.d
        i += 1
    return h

def diophantine(max_D):
    best_x = 0
    best_D = -1
    x = 0
    for D in range(2,max_D+1):
        if (D ** 0.5).is_integer():
            continue
        if (x:=pell_solution(D)) > best_x:
            best_x,best_D = x,D
    return best_D

print(diophantine(1000))
