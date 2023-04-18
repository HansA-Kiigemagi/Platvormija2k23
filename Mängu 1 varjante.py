import pygame as pg
from sys import exit
import pygame.image
from pygame import Rect
from random import randint



pg.init()
# Ekraan ja muu põhi
screen = pg.display.set_mode((800,600))
pg.display.set_caption("Mäng")
clock = pg.time.Clock()

# Tausta ja muu import
x = 200
y = 470
background_image = pygame.image.load("taust.png")
tegelase_image_vasak = pg.image.load("Nimetu_vasak.png")
tegelase_image_vasak_rect = tegelase_image_vasak.get_rect(bottomleft = (x, y))
tegelase_image_parem = pg.image.load("Nimetu_parem.png")
tegelase_image_parem_rect = tegelase_image_parem.get_rect(bottomleft = (x, y))

# Liikumiskirus
spd = 5

# Hüppe parameetrid
isJump = False
jump_frames = 10


# Ruudu koordinaadid
suund = "parem"

tegelane = pg.Surface((30,30))
tegelane.fill((255,0,0))

# Kastike, mida tegelane hakkab kinni püüdma
a = 0
b = 0
külg1 = 200
külg2 = 50
rect = pg.Rect(a, b, 200, 50)

#Platvorm
c = 100
d = 500
plat_surf = pg.Surface((100, 20))
plat_rect = plat_surf.get_rect(bottomleft = (c, d))

#Punktid
punkte = 0

#.....
gravitatsioon = 0


while True:
    pg.time.delay(10)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()


    screen.blit(background_image, (0, 0))


    screen.blit(plat_surf, plat_rect)

    #hüpe
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_UP:
            gravitatsioon = -15
    #paremale-vasakule
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_RIGHT:
            tegelase_image_parem_rect.x += 10
            tegelase_image_vasak_rect.x += 10
        if event.key == pg.K_LEFT:
            tegelase_image_parem_rect.x -= 10
            tegelase_image_vasak_rect.x -= 10


    gravitatsioon += 1
    tegelase_image_parem_rect.y += gravitatsioon
    tegelase_image_vasak_rect.y += gravitatsioon

    #Tegelane ei lähe madalamale, kui 600 ('püsib maapinnal')
    if tegelase_image_vasak_rect.bottom >= 600:
        tegelase_image_vasak_rect.bottom = 600
    if tegelase_image_parem_rect.bottom >= 600:
        tegelase_image_parem_rect.bottom = 600
    #Tegelane ei lähe mänguaknast välja
    if tegelase_image_parem_rect.y < 0:
        tegelase_image_parem_rect.y = 0
    if tegelase_image_vasak_rect.y < 0:
        tegelase_image_vasak_rect.y = 0
    #Kui tegelane liigub ühest küljes välja, ilmub ta teisest küljest
    if tegelase_image_parem_rect.x < 0:
        tegelase_image_parem_rect.x = 800
    if tegelase_image_vasak_rect.x < 0:
        tegelase_image_vasak_rect.x = 800
    if tegelase_image_parem_rect.x > 800:
        tegelase_image_parem_rect.x = 0
    if tegelase_image_vasak_rect.x > 800:
        tegelase_image_vasak_rect.x = 0
    #suund
    if suund == "parem":
        screen.blit(tegelase_image_parem, tegelase_image_parem_rect)
    elif suund == "vasak":
        screen.blit(tegelase_image_vasak, tegelase_image_vasak_rect)
    #kokkupõrge
    if tegelase_image_parem_rect.colliderect(plat_rect):
        punkte += 1
        plat_rect.bottomleft = (randint(0, 700), randint(0, 550))
        #Platvorm, mida püütakse müüdab iga kord suurust
        """plat_rect.width = (randint(10,100))
        plat_rect.height = (randint(10, 100))"""

    pg.display.update()
    clock.tick(60)




#hüpe
"""    if not(isJump):
        if key[pygame.K_UP]:
            isJump = True
    else:
        if jump_frames >= -10:
            y -= (jump_frames * abs(jump_frames)) * 0.5
            jump_frames -= 1
        else:
            jump_frames = 10
            isJump = False"""

#liikumine nooltega
"""    key = pg.key.get_pressed()

    if key[pg.K_RIGHT]:
        suund = "parem"
        if x + spd <= 770:
            x += spd
    if key[pg.K_LEFT]:
        suund = "vasak"
        if x - spd >= 0:
            x -= spd"""