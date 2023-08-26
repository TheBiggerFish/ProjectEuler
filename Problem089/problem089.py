# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 89

# Find the number of characters saved by writing each of the roman numerals in roman.txt in their minimal form.


values = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}


def roman_to_arabic(roman: str):
    sum_ = 0
    while roman != '':
        if len(roman) > 1 and values[roman[0]] < values[roman[1]]:
            sum_ += values[roman[1]] - values[roman[0]]
            roman = roman[2:]
        else:
            sum_ += values[roman[0]]
            roman = roman[1:]
    return sum_


def arabic_to_roman(arabic):
    roman = ''
    while arabic != 0:
        for symbol in values:
            if arabic >= values[symbol]:
                arabic -= values[symbol]
                roman += symbol
                break
    return roman


def chars_saved(filename):
    saved = 0
    with open(filename, 'r') as f:
        for line in f:
            old = line.rstrip()
            new = arabic_to_roman(roman_to_arabic(old))
            saved += len(old) - len(new)
    return saved


print(chars_saved('Problem089/roman.txt'))
