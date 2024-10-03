class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return str(self.x) + "," + str(self.y)
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    def __neg__(self):
        return self.scaled(-1)
    def add_changing(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
    def scale(self, scalar):
        self.x = self.x * scalar
        self.y = self.y * scalar
    def scaled(self, scalar):
        return Vec(self.x * scalar, self.y * scalar)
    def __mul__(self, scalar): # dubious, because this will be used when the scalar is the 2nd operand (v * s)
        return Vec(self.x * scalar, self.y * scalar)
    __rmul__ = __mul__ # that's the way
    def __rmul__(self, scalar): # equivalent to
        return Vec(self.x * scalar, self.y * scalar)

    
v = Vec(1,1)
w = Vec(10,10)
print((w * 2)) # w.__mul__(2)
# print((2 * (-w)) + Vec(3,6))
print(2 * w) # first attempts to do (2).__mul__(w); but then the NotImplemented exception is thrown and w.__rmul__(2) is run

