# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 40

# An irrational decimal fraction is created by concatenating the positive integers:
#     0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#     d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


def gen_concats(max_):
    string = ''
    i = 1
    while len(string) < max_:
        string += str(i)
        i += 1
    return string

which = [1,10,100,1000,10000,100000,1000000]
d = gen_concats(max(which))
product = 1
for num in which:
    product *= int(d[num-1])
print(product)