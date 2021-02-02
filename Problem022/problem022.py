# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 22

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?


import csv

def get_word_value(word):
    value = 0
    for char in word:
        value += ord(char)-64
    return value

def get_total_score(names):
    total = 0
    for i in range(len(names)):
        total += (i+1) * get_word_value(names[i])
    return total

with open('Problem022/names.txt') as csvfile:
    reader = csv.reader(csvfile,delimiter=',',quotechar='"')
    names = reader.__next__()
    print(get_total_score(sorted(names)))

