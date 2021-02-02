# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 51

# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 
#       56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
# Consequently 56003, being the first member of this family, is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.


from itertools import permutations as perms

# Generate all primes lower than max_ with the Sieve of Eratosthenes
def sieve(max_):
    composite = set()
    for i in range(2,max_):
        if i in composite:
            continue
        for j in range(i**2,max_,i):
            composite.add(j)
    return set(range(2,max_)).difference(composite)

def get_patterns(n,digits):
    return set([tuple(list(item)+['']) for item in perms(['']*(digits-n-1)+['*']*(n))])
    
def num_to_list(num,len_):
    lst = []
    size = len(str(num))
    for i in range(size):
        lst.append(num // (10**(size-i-1)) % 10)
    while len(lst) < len_:
        lst = [0] + lst
    return lst

def list_to_num(lst):
    num = 0
    for i in range(len(lst),0,-1):
        num += 10**(i-1) * lst[-i]
    return num

def prime_digit_replacements(n,digits):
    primes = sieve(10**digits)
    patterns = get_patterns(n,digits)
    for fill in range(1,10**(digits-n),2):
        num_list = num_to_list(fill,digits-n)
        for pattern in patterns:
            lst = list(pattern)
            
            found = 0
            for i in range(digits):
                if found == digits-n:
                    break
                if lst[i] == '':
                    lst[i] = num_list[found]
                    found += 1
                    
            prime_list = []
            for i in range(10):
                cpy = [item if item != '*' else i for item in lst]
                # if lst[0] == 0 and lst[3] == 0 and lst[4] == 7:
                #     print(cpy,count)
                num = list_to_num(cpy)
                if num in primes:
                    prime_list.append(num)
            if len(prime_list) >= 8:
                print(min(prime_list))

prime_digit_replacements(3,6)