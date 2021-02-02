# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 80

# For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.


from EulerLib.root import IntegerSquareRoot

def digital_sum(list_:list) -> int:
    return sum(n for n in list_)

def natural_square_sums(max_n:int,digits:int):
    sum_ = 0
    for n in range(1,max_n+1):
        if not (n**0.5).is_integer():
            sum_ += digital_sum(IntegerSquareRoot(n,digits).value)
            print(n,len(IntegerSquareRoot(n,digits).value), digital_sum(IntegerSquareRoot(n,digits).value))
    return sum_

print(natural_square_sums(100,100))