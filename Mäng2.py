import pygame as pg


pg.init()
screen = pg.display.set_mode((1200, 600))


pilt = pg.image.load("Uus kaust/pilt.jfif").convert_alpha()

background = pg.image.load("Uus kaust/taust.png").convert_alpha()
backgroundRect = background.get_rect(topright = (0,0))

x = 0
y = 0

pg.key.set_repeat(15)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                y += 10
            if event.key == pg.K_UP:
                y -= 10
            if event.key == pg.K_RIGHT:
                x += 10
            if event.key == pg.K_LEFT:
                x -= 10
#   pilti saab noolega liigutada vasakule, paremale, üles ja alla


    screen.fill((0, 0, 0))
    screen.blit(pilt, (x, y))
#    screen.blit(background, backgroundRect)
    pg.display.update()


