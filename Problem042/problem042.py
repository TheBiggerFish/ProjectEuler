# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 42

# The nth term of the sequence of triangle numbers is given by, t_n = ½n(n+1); so the first ten triangle numbers are:
#          1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. 
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt, how many are triangle words?


import csv 

def get_word_value(word):
    value = 0
    for char in word:
        value += ord(char)-64
    return value

def find_triangle_words(lst,tri_nums):
    total = 0
    for word in lst:
        if get_word_value(word) in tri_nums:
            total += 1
    return total

tri_nums = [int(n*(n+1)/2) for n in range(1,50)]
with open('Problem42/words.txt') as csvfile:
    reader = csv.reader(csvfile,delimiter=',',quotechar='"')
    words = reader.__next__()
    print(find_triangle_words(sorted(words),tri_nums))