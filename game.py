from graphx import *
from utils import *
import pickle


class Type(Enum):
    def __init__(self, color, desc):
        self.color = color
        self.desc = desc


ROCK = Type(Color.BLACK, 'solid block')
AIR = Type(Color.WHITE, 'transparent block')
SMOKE = Type(Color.GREY, 'non-transparent block')
HOME = Type(Color.GREEN, 'home zone')
BASE = Type(Color.RED, 'base zone')
PLANT = Type(Color.ORANGE, 'plant zone')
TRAP = Type(Color.YELLOW, 'trap')


class World:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.map = [[AIR for _ in range(self.w)] for _ in range(self.h)]

    def add(self, block, x, y):
        self.map[y][x] = block

    def load(self, name):
        with open('maps/' + name, 'rb') as file:
            self.map = pickle.load(file)

    def save(self, name):
        with open('maps/' + name, 'wb') as file:
            pickle.dump(self.map, file)


class Playground:
    def __init__(self, map, ):
        self.map =