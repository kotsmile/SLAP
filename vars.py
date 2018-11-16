SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SLPIXEL = 15
SLWIDTH = SCREEN_WIDTH // SLPIXEL
SLHEIGHT = SCREEN_HEIGHT // SLPIXEL

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (211, 211, 211)
ORANGE = (255, 165, 0)
BRIGHT_YELLOW = (255, 255, 150)
PURPLE = (255, 51, 255)
DARK_RED = (180, 0, 0)
DARK_GREEN = (0, 180, 0)


class Block:
    def __init__(self, color, desc, name):
        self.color = color
        self.desc = desc
        self.name = name

    def same(self, b):
        return b.name == self.name



BOX = Block(BLACK, 'box - solid block', 'box')
AIR = Block(WHITE, 'air - transparent block', 'air')
SMOKE = Block(GREY, 'smoke - non-transparent block', 'smoke')
HOME = Block(GREEN, 'home - green spawn', 'home')
BASE = Block(RED, 'base - red spawn', 'base')
PLANT = Block(ORANGE, 'plant - plant zone', 'plant')
DEV = Block(PURPLE, 'dev block', 'dev')

