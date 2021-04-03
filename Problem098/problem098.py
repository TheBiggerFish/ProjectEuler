# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 98

# What is the largest square number formed by any member of an anagramic pair?


from itertools import permutations

def is_square(num) -> bool:
    if num == 0:
        return False
    return float(num**0.5).is_integer()

def get_value(word,mapping):
    if mapping[word[0]] == '0':
        return 0
    return int(''.join([mapping[letter] for letter in word]))

def square_pair(w1:str,w2:str) -> int:
    letters = sorted(set(w1))
    mappings = [{letters[i]:perm[i] for i in range(len(letters))} for perm in permutations(['1','2','3','4','5','6','7','8','9','0'],len(letters))]
    max_val = 0
    for mapping in mappings:
        val1 = get_value(w1,mapping)
        if not is_square(val1):
            continue
        val2 = get_value(w2,mapping)
        if not is_square(val2):
            continue
        max_val = max(max_val,val1,val2)
        print(max_val,w1,w2,val1,val2,mapping)

    return max_val

with open('Problem098/words.txt') as f:
    dictionary = set(f.read().strip('"').split('","'))
    anagrams = {}
    for word in dictionary:
        ordered = ''.join(sorted(word))
        anagrams[ordered] = [word] if ordered not in anagrams else anagrams[ordered] + [word]
    anagrams = {key:anagrams[key] for key in list(filter(lambda key: len(anagrams[key]) > 1,anagrams))}
    # print(anagrams)

    max_val = 0
    for key in anagrams:
        max_val = max(max_val,square_pair(anagrams[key][0],anagrams[key][1]))
    print(max_val)