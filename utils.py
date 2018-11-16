import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y)

    def __mul__(self, a):
        return Vector(a * self.x, a * self.y)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def in_radius(self, radius, vector):
        return radius >= abs(self - vector)


# UP = Vector(0, 1)
# DOWN = Vector(0, -1)
# RIGHT = Vector(1, 0)
# LEFT = Vector(-1, 0)
