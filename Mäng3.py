import pygame as pg


pg.init()
screen = pg.display.set_mode((1200, 600))
clock = pg.time.Clock()

pilt = pg.image.load("Uus kaust/pilt.jfif").convert_alpha()

background_image = pg.image.load("Uus kaust/taust.png").convert_alpha()

jumpCount = 10
isJump = False

x = 0
y = 0

spd = 5
#pg.key.set_repeat(15)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    key = pg.key.get_pressed()
    if key[pg.K_RIGHT]:
        x += spd
    if key[pg.K_LEFT]:
        x -= spd

    if not (isJump):  # Checks is user is not jumping
        if key[pg.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:  # This will execute if our jump is finished
            jumpCount = 10
            isJump = False
    if key[pg.K_DOWN]:
        y += spd
#   pilti saab noolega liigutada vasakule, paremale, üles ja alla


    screen.fill((0, 0, 0))
    screen.blit(pilt, (x, y))
#    screen.blit(background_image, (0, 0))
    pg.display.update()
    clock.tick(60)