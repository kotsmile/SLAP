import pickle
from enum import auto, Enum
from graphx import *
import time


class Result(Enum):
    NONE = auto()
    BOMB = auto()
    BULL = auto()
    TRAP = auto()
    TICK = auto()


class Action(Enum):
    JUMP = auto()
    LEFT = auto()
    RIGHT = auto()
    SHOOT_L = auto()
    SHOOT_R = auto()


class World:
    def __init__(self, name, width, height):
        self.name = name
        self.w = width
        self.h = height
        self.map = [[AIR for _ in range(self.h)] for _ in range(self.w)]

    def add(self, block, x, y):
        self.map[x][y] = block

    def load(self):
        with open('maps/' + self.name + '.slw', 'rb') as file:
            self.map = pickle.load(file)

    def save(self):
        with open('maps/' + self.name + '.slw', 'wb') as file:
            pickle.dump(self.map, file)

    def get(self, x, y):
        return self.map[x][y]

    def green(self):
        print()
        for x in range(self.w):
            for y in range(self.h):
                if self.map[x][y].same(HOME):
                    return slpixel_to_pixel(Vector(x, y))

    def red(self):
        for x in range(self.w):
            for y in range(self.h):
                if self.map[x][y].same(BASE):
                    return slpixel_to_pixel(Vector(x, y))


class Sprite:
    def __init__(self, color, size):
        self.position = Vector()
        self.velocity = Vector()
        self.color = color
        self.size = size

    def update(self, pg):
        pass


class SmallSprite(Sprite):
    def __init__(self, color):
        Sprite.__init__(self, color, 1)


class BigSprite(Sprite):
    def __init__(self, color):
        Sprite.__init__(self, color, 15)


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
        BigSprite.__init__(self, YELLOW)
        self.radius = 1

    def update(self, pg):
        for p in pg.players:
            if p.position.in_radius(self.radius, self.position):
                return Result.TRAP, p


class Bomb(BigSprite):
    def __init__(self):
        BigSprite.__init__(self, BLUE)
        self.timer = 100

    def update(self, pg):
        self.timer -= 1
        if self.timer <= 0:
            return Result.BOMB, None
        else:
            return Result.TICK, self.timer


class Player(BigSprite):
    def __init__(self, color, spawn):
        BigSprite.__init__(self, color)
        self.position = spawn
        self.next_velocity = Vector(0, 0)
        self.hp = 3
        self.reload = 10
        self.score = 0

    def update(self, pg):
        pos_d = pixel_to_slpixel(self.position) + Vector(0, 1)
        if pg.world.get(pos_d.x, pos_d.y).same(AIR):
            self.velocity += Vector(0, 1)
            self.position += self.velocity
        else:
            self.velocity = Vector(0, 0)

        pos = self.position
        x_d = pos.x
        y_d = pos.y

        up_p = pos + Vector(0, -1)
        left_p = pos + Vector(-1, 0)

        if pg.world.get(pixel_to_slpixel(up_p).x. pixel_to_slpixel(up_p).y).same(BOX):
            pass



    def do(self, act, pg):
        if act is Action.LEFT:
            new_pos = self.position + Vector(-1, 0) * 5
            slpos = pixel_to_slpixel(new_pos)
            if not pg.world.get(slpos.x, slpos.y).same(BOX):
                self.position = new_pos

        elif act is Action.RIGHT:
            new_pos = self.position + Vector(1, 0) * 5
            slpos = pixel_to_slpixel(new_pos + Vector(SLPIXEL - 1, 0))
            if not pg.world.get(slpos.x, slpos.y).same(BOX):
                self.position = new_pos

        elif act is Action.JUMP:
            pos = pixel_to_slpixel(self.position) + Vector(0, 1)
            if pg.world.get(pos.x, pos.y).same(BOX):
                self.velocity += Vector(0, -15)
                self.position += self.velocity


class GreenPlayer(Player):
    def __init__(self, spawn):
        Player.__init__(self, DARK_GREEN, spawn)


class RedPlayer(Player):
    def __init__(self, spawn):
        Player.__init__(self, DARK_RED, spawn)


class Playground:
    def __init__(self, world):
        self.world = world
        self.world.load()
        self.players = [GreenPlayer(self.world.green())]
        self.sprites = []


class SLAPGame:
    def __init__(self, name):
        self.world = World(name, SLWIDTH, SLHEIGHT)
        self.pg = Playground(self.world)
        self.gx = GraphX(pg=self.pg)
        self.state = True

    def new(self):
        pass

    def run(self):
        while self.state:
            self.gx.draw()
            time.sleep(0.0001)
            for event in pygame.event.get():

                if event.type == QUIT:
                    return

            if pygame.key.get_pressed()[K_d]:
                self.pg.players[0].do(Action.RIGHT, self.pg)

            if pygame.key.get_pressed()[K_a]:
                self.pg.players[0].do(Action.LEFT, self.pg)

            if pygame.key.get_pressed()[K_SPACE]:
                self.pg.players[0].do(Action.JUMP, self.pg)

            if pygame.key.get_pressed()[K_LEFT]:
                self.pg.players[0].do(Action.SHOOT_L, self.pg)

            if pygame.key.get_pressed()[K_RIGHT]:
                self.pg.players[0].do(Action.SHOOT_R, self.pg)

            self.pg.players[0].update(self.pg)
