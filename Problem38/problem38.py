# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 38

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?


def is_pan(str_):
    for i in range(1,10):
        if str(i) not in str_:
            return False
    return True


max_ = 0
for i in range(9,10000):
    number = ''
    for j in range(1,9):
        number += str(i*j)
        if len(number) > 9:
            break
        if len(number) == 9:
            if is_pan(number):
                if int(number) > max_:
                    max_ = int(number)
print(max_)