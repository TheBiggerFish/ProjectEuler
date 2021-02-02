# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 68

# Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.
# It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
# By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.
# Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?


from itertools import permutations as perms
from math import log10 as log

class Ngon:
    def __init__(self,n):
        self.n = n
        self.__inner = [-1]*n
        self.__outer = [-1]*n

    @staticmethod
    def gen_ngons(n):
        lst = []
        for perm in perms([i for i in range(1,n*2+1)]):
            if perm[0] > n + 1:
                break
            ng = Ngon(n)
            ng.set_outer(list(perm[:n]))
            ng.set_inner(list(perm[n:]))
            lst.append(ng)
        return list(set(filter(lambda ng: ng.is_valid(),lst)))

    def get_sum(self):
        return self.__outer[0] + self.__inner[0] + self.__inner[1]

    def test_sum(self,sum_):
        for i in range(self.n):
            if self.__outer[i] + self.__inner[i] + self.__inner[(i+1)%self.n] != sum_:
                return False
        return True

    def is_valid(self):
        sum_ = self.get_sum()
        return self.test_sum(sum_)

    def set_inner(self,inner):
        self.__inner = inner

    def set_outer(self,outer):
        self.__outer = outer

    def __str__(self):
        str_ = ''
        for i in range(self.n):
            str_ += str(self.__outer[i])
            str_ += str(self.__inner[i])
            str_ += str(self.__inner[(i+1)%self.n])
        return str_

    def __eq__(self,other):
        if self.n != other.n:
            return False
        for i in range(self.n):
            if self.__inner != other.__inner[i:] + other.__inner[:i]:
                continue
            if self.__outer != other.__outer[i:] + other.__outer[:i]:
                return False
            return True
        return False

    def __hash__(self):
        power = int(log(self.n))+1
        hash_ = 0
        start = self.__outer.index(min(self.__outer))
        i = self.n-1
        for spot in list(range(start,self.n)) + list(range(start)):
            # print(hash_)
            hash_ += self.__inner[spot] * (10**(i*power))
            hash_ += self.__outer[spot] * (10**(i*power+self.n))
            i -= 1
        return hash_

def max_branch(n,max_value):
    max_ = 0
    for item in Ngon.gen_ngons(n):
        i_num = int(str(item))
        if i_num < max_value:
            if i_num > max_:
                max_ = i_num
    return max_

print(max_branch(5,10**16))