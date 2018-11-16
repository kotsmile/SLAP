import pygame
from pygame.locals import *
from utils import *
from vars import *

pygame.init()


def slpixel_to_pixel(v):
    return Vector(v.x * SLPIXEL, v.y * SLPIXEL)


def pixel_to_slpixel(v):
    return Vector(v.x // SLPIXEL, v.y // SLPIXEL)


def draw_sq(surface, v, c, s):
    r = pygame.Rect((v.x, v.y), (s, s))
    pygame.draw.rect(surface, c, r)


class GraphX:
    def __init__(self, pg=None, world=None):
        self.ws = SCREEN_WIDTH
        self.hs = SCREEN_HEIGHT
        self.width = SLWIDTH
        self.height = SLHEIGHT
        self.pg = pg
        if not pg:
            self.world = world
        else:
            self.world = pg.world

        self.screen = pygame.display.set_mode((self.ws, self.hs), 0, 32)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        self.surface.fill(WHITE)

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                draw_sq(self.surface, slpixel_to_pixel(Vector(x, y)), self.world.map[x][y].color, SLPIXEL)
        if self.pg:
            for p in self.pg.players:
                draw_sq(self.surface, Vector(p.position.x, p.position.y), p.color, p.size)

            for s in self.pg.sprites:
                draw_sq(self.surface, Vector(s.position.x, s.position.y), s.color, s.size)

        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()
