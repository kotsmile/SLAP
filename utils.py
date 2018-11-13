from enum import Enum


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y)

    def __mul__(self, a):
        return Vector(a * self.x, a * self.y)

    def __abs__(self):
        return self.x ** 2 + self.y ** 2




