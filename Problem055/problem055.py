# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 55

# How many Lychrel numbers are there below ten-thousand?


def is_lychrel(num,depth,max_depth):
    if depth > max_depth:
        return True
    if depth > 0 and str(num) == str(num)[::-1]:
        return False
    return is_lychrel(num + int(str(num)[::-1]),depth+1,max_depth)

def find_lychrel(max_num,max_depth):
    count = 0
    for i in range(1,max_num):
        if is_lychrel(i,0,max_depth):
            print(i)
            count += 1
    return count

print(find_lychrel(10**4,50))