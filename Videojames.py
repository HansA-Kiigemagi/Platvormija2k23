import pygame as pg
from sys import exit
import pygame.image
from random import randint


pg.init()
# Ekraan ja muu põhi
screen = pg.display.set_mode((800,600))
pg.display.set_caption("Mäng")
clock = pg.time.Clock()

# Tausta ja muu import
background_image = pygame.image.load("taust.png")
tegelase_image_vasak = pg.image.load("Nimetu_vasak.png")
tegelase_image_parem = pg.image.load("Nimetu_parem.png")


# Liikumiskiirus
spd = 5

# Hüppe parameetrid
isJump = False
jump_frames = 10

#Maapind ja sellega seonduv
a = 200
b = 500
kuju = pg.Surface((100, 20))

# Ruudu koordinaadid
x = 0
y = 570
suund = "parem"

tegelane = pg.Surface((30,30))
tegelane.fill((255,0,0))




while True:
    pg.time.delay(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    key = pg.key.get_pressed()

    if key[pg.K_RIGHT]:
        suund = "parem"
        if x >= 800:
            x = 0
        else:
            x += spd
    if key[pg.K_LEFT]:
        suund = "vasak"
        if x <= 0:
            x = 800
        else:
            x -= spd
    if not(isJump):
        if key[pygame.K_UP]:
            isJump = True
    else:
        if jump_frames >= -10:
            y -= (jump_frames * abs(jump_frames)) * 0.5
            jump_frames -= 1
        else:
            jump_frames = 10
            isJump = False


    screen.blit(background_image, (0, 0))

    if suund == "parem":
        screen.blit(tegelase_image_parem, (x, y))
    elif suund == "vasak":
        screen.blit(tegelase_image_vasak, (x, y))

# kui tegelenae puutub kuju, siis ilmub teine tasand välja(radnint)
    a = randint(0, 770)
    b = randint(0, 600)
    screen.blit(kuju, (a,b))

    pg.display.update()
    clock.tick(60)