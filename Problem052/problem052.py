# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 52

# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

    
def same_digits(num1,num2):
    return sorted(str(num1)) == sorted(str(num2))

def find_same_digits(digits,max_mult):
    for i in range(10**(digits-1),int(10**digits/6)+1):
        for mult in range(2,max_mult+1):
            if not same_digits(i,i*mult):
                break
            if mult == max_mult:
                return (i,i*2,i*3,i*4,i*5,i*6)
print(find_same_digits(6,6))