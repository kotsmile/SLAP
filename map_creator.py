from graphx import *


keymap = '''
====KEYMAP====
s - SAVE
l - LOAD
> - next block
< - previous block
LMB / d - draw
'''


def main():
    world = World('no_name', SLWIDTH, SLHEIGHT)
    gx = GraphX(world=world)

    gx.draw()

    pick = 1

    blocks = [AIR, BOX, HOME, BASE, PLANT, SMOKE]

    perm_n = True
    perm_p = True

    print(keymap)
    print(blocks[pick].desc)
    while True:
        if pygame.key.get_pressed()[K_LEFT] and perm_n:

            pick += 1
            pick = pick % len(blocks)
            print(blocks[pick].desc)

        perm_n = not pygame.key.get_pressed()[K_LEFT]

        if pygame.key.get_pressed()[K_RIGHT] and perm_p:
            pick -= 1
            pick = pick % len(blocks)
            print(blocks[pick].desc)

        perm_p = not pygame.key.get_pressed()[K_RIGHT]

        if pygame.key.get_pressed()[K_s]:
            name = input('Enter name > ')
            world.name = name
            world.save()

        if pygame.key.get_pressed()[K_l]:
            name = input('Enter name > ')
            world.name = name
            world.load()

        for event in pygame.event.get():

            if event.type == QUIT:
                return

        if pygame.mouse.get_pressed()[0] or pygame.key.get_pressed()[K_d]:
            pos = pixel_to_slpixel(Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
            world.add(blocks[pick], pos.x, pos.y)

        gx.draw()


if __name__ == '__main__':
    main()
