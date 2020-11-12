# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 26

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
# https://eli.thegreenplace.net/2009/02/25/project-euler-problem-26/
# https://mathworld.wolfram.com/DecimalExpansion.html


# Probably very over-complicated
def cycle_length(digit_list,max_cycle):
    # print(digit_list)
    for i in range(1,max_cycle+1):
        match = False
        started = False
        for j in range(len(digit_list)-i):
            # print(i,j,started,match,digit_list)
            if digit_list[j] != digit_list[i+j] and started:
                match = False
                break
            elif digit_list[j] == digit_list[i+j] != 0 and not started:
                started = True
            elif digit_list[j] == digit_list[i+j] != 0:
                match = True
        if match:
            return i
    return -1

def divide(numer,denom,max_depth):
    div = []
    for _ in range(max_depth):
        div.append(numer//denom)
        numer -= div[-1] * denom
        numer *= 10
    return div

def longest_recip_cycles(min_value,max_value,precision,max_cycle):
    max_digit=-1
    max_length=0
    for i in range(min_value,max_value+1):
        length = cycle_length(divide(1,i,precision),max_cycle)
        if length > max_length:
            max_length = length
            max_digit = i
    return max_digit,max_length

print(longest_recip_cycles(11,1000,precision=2000,max_cycle=2000))