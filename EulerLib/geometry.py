class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x * (10**10) + self.y

    def __lt__(self,other):
        if self.y < other.y:
            return True
        return self.x < other.x

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def manhattan_distance(self,other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def euclidean_distance(self,other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5