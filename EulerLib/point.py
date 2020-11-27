class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.x)

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.y * 10**10 + self.x

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __lt__(self,other):
        return self.x > other.x or (self.x == other.x and self.y > other.y)