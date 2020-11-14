# Written by Cameron Haddock
# Written as a solution to Project Euler's Problem 41

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    for divisor in range(6, int(n**0.5) + 1, 6):
        if n % (divisor - 1) == 0 or n % (divisor + 1) == 0:
            return False
    return True

def is_pan(number,digits):
    found = [False]*digits
    i = 0
    while number > 0:
        n = number % 10
        number //= 10
        if n <= 0 or n > digits:
            return False
        if found[n-1]:
            return False
        found[n-1] = True
        i += 1
    if i != digits:
        return False
    return True

def find_max_pan(digits):
    for i in range(10**(digits)-1,10**(digits-1),-2):
        if is_pan(i,digits):
            yield i
    return -1

def find_prime_pan(digits):
    pan = find_max_pan(digits)
    for num in pan:
        if is_prime(num):
            return num
    return -1

def main():
    print(find_prime_pan(digits=8))

if __name__ == "__main__":
    main()