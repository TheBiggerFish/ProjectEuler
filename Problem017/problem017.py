# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.


from math import floor 

words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

def word(number):
    final = ''
    if number in words:
        final = words[number]
        number = 0
    if number >= 1000000:
        final += word(floor(number/1000000)) + ' million '
        number %= 1000000
    if number >= 1000:
        final += word(floor(number/1000)) + ' thousand '
        number %= 1000
    if number >= 100:
        final += word(floor(number/100)) + ' hundred '
        number %= 100
        if number > 0:
            final += 'and '
    if number >= 20:
        final += word(floor(number/10)*10) + ' '
        number %= 10
    if number > 0:
        final += words[number]
    return final
    
def loop(max_):
    sum_ = 0
    for i in range(1,max_+1):
        print(word(i))
        sum_ += len(word(i).replace(' ',''))
    return sum_

print(loop(1000))