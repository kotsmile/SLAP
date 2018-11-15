import pickle
from enum import auto, Enum
from utils import *
from graphx import GraphX

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SLPIXEL = 15
SLWIDTH = SCREEN_WIDTH // SLPIXEL
SLHEIGHT = SCREEN_HEIGHT // SLPIXEL


def slpixel_to_pixel(v):
    return Vector(v.x * SLPIXEL, v.y * SLPIXEL)


def pixel_to_slpixel(v):
    return Vector(v.x // SLPIXEL, v.y // SLPIXEL)


class Block:
    def __init__(self, color, desc, name):
        self.color = color
        self.desc = desc
        self.name = name


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (211, 211, 211)
ORANGE = (255, 165, 0)
BRIGHT_YELLOW = (255, 255, 150)


class Result(Enum):
    NONE = auto()
    BOMB = auto()
    BULL = auto()
    TRAP = auto()
    TICK = auto()


BOX = Block(BLACK, 'box - solid block', 'box')
AIR = Block(WHITE, 'air - transparent block', 'air')
SMOKE = Block(GREY, 'smoke - non-transparent block', 'smoke')
HOME = Block(GREEN, 'home - green spawn', 'home')
BASE = Block(RED, 'base - red spawn', 'base')
PLANT = Block(ORANGE, 'plant - plant zone', 'plant')
TRAP = Block(YELLOW, 'trap', 'trap')


class World:
    def __init__(self, name, width, height):
        self.name = name
        self.w = width
        self.h = height
        self.map = [[AIR for _ in range(self.h)] for _ in range(self.w)]

    def add(self, block, x, y):
        self.map[x][y] = block

    def load(self):
        with open('maps/' + self.name + '.sl', 'rb') as file:
            self.map = pickle.load(file)

    def save(self):
        with open('maps/' + self.name + '.sl', 'wb') as file:
            pickle.dump(self.map, file)

    def get(self, x, y):
        return self.map[x][y]

    def green(self):
        for x in range(self.w):
            for y in range(self.h):
                if self.map[x][y] is HOME:
                    return pixel_to_slpixel(Vector(x, y))

    def red(self):
        for x in range(self.w):
            for y in range(self.h):
                if self.map[x][y] is BASE:
                    return pixel_to_slpixel(Vector(x, y))


class Sprite:
    def __init__(self, color):
        self.position = Vector()
        self.velocity = Vector()
        self.color = color
        self.size = 1

    def update(self, pg):
        pass


class SmallSprite(Sprite):
    def __init__(self, color):
        self.size = 1
        Sprite.__init__(self, color)


class BigSprite(Sprite):
    def __init__(self, color):
        self.size = SLPIXEL
        Sprite.__init__(self, color)


class Bullet(SmallSprite):
    def __init__(self, velocity):
        SmallSprite.__init__(self, BRIGHT_YELLOW)
        self.radius = 0
        self.velocity = velocity

    def update(self, pg):
        self.position = self.position + self.velocity

        for p in pg.players:
            if p.position.in_radius(self.radius, self.position):
                return Result.BULL, p


class Trap(BigSprite):
    def __init__(self):
        Sprite.__init__(self, YELLOW)
        self.radius = 1

    def update(self, pg):
        for p in pg.players:
            if p.position.in_radius(self.radius, self.position):
                return Result.TRAP, p


class Bomb(BigSprite):
    def __init__(self):
        Sprite.__init__(self, BLUE)
        self.timer = 100

    def update(self, pg):
        self.timer -= 1
        if self.timer <= 0:
            return Result.BOMB, None
        else:
            return Result.TICK, self.timer


class Player(BigSprite):
    def __init__(self, color, spawn):
        Sprite.__init__(self, color)
        self.position = spawn

    def update(self, pg):
        # gravity force
        pass

    def move(self, velocity):
        self.position = self.position + velocity


class GreenPlayer(Player):
    def __init__(self, spawn):
        Player.__init__(self, GREEN, spawn)


class RedPlayer(Player):
    def __init__(self, spawn):
        Player.__init__(self, RED, spawn)


class Playground:
    def __init__(self, world):
        self.world = world
        self.players = [GreenPlayer(self.world.green()), RedPlayer(self.world.red())]
        self.sprites = []


class Game:
    def __init__(self, name):
        self.world = World(name, SLWIDTH, SLHEIGHT)
        self.pg = Playground(world)
        self.gx = GraphX(pg=self.pg)
        self.state = True

    def run(self):
        while self.state:
            pass
