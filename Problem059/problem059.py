# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 59

# Using cipher.txt, a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.


def repeated_xor(key,values):
    rv = []
    for i in range(len(values)):
        rv.append(chr(values[i] ^ key[i%3]))
    return rv

def frequency(chars):
    for i in range(len(chars)-5):
        if ''.join(chars[i:i+5]) == 'Euler':
            return True
    return False

def decrypt(filename):
    with open(filename) as f:
        chars = []
        for line in f:
            chars += line.strip().split(',')
        chars = [int(c) for c in chars]

        for a in range(ord('a'),ord('z')+1):
            for b in range(ord('a'),ord('z')+1):
                for c in range(ord('a'),ord('z')+1):
                    key = [a,b,c]
                    dec = repeated_xor(key,chars)
                    if frequency(dec):
                        return sum([ord(c) for c in dec])
    return -1

print(decrypt('Problem59/cipher.txt'))