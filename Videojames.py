import pygame as pg
from sys import exit

import pygame.image


# Ekraan ja muu põhi
pg.init()
screen = pg.display.set_mode((800,600))
pg.display.set_caption("Mäng")
clock = pg.time.Clock()

mäng_käib = True

# Tausta ja muu import
taust = pg.image.load("taust.png").convert()
tegelase_image_vasak = pg.image.load("Nimetu_vasak.png").convert()

    # Surface ja rectangle

# Tegelane

class Tegelane(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.image.load("Nimetu_parem.png").convert()
        self.rect = self.surf.get_rect(midbottom = (15,600))
        self.gravitatsioon = 0

    def sisend(self):
        nupp = pg.key.get_pressed()
        if nupp[pg.K_UP] and self.rect.bottom >= 600:
            self.gravitatsioon = -20

    def gravitatsiooni_mõju(self):
        self.gravitatsioon += 1
        self.rect.y += self.gravitatsioon
        if self.rect.bottom >= 600:
            self.rect.bottom = 600

tegelane = pg.sprite.GroupSingle()
tegelane.add(Tegelane())
# Platvorm
plat1_surf = pg.Surface((30,20))
plat1_rect = plat1_surf.get_rect(midbottom = (200, 600))



# Mängu loop
while True:

    # Väljumise loop
    for event in pg.event.get():

        # Väljumiskäsk
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        # Nupuvajutused
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and tegelase_rect.bottom == 600:
                tegelane_gravitatsioon = -20

            if event.key == pg.K_RIGHT:
                    tegelase_rect.x += 15

        # Joonistamised

    if mäng_käib:
        # Taust
        screen.blit(taust,(0,0))

        # Platvormid
        screen.blit(plat1_surf, plat1_rect)

        tegelane.draw(screen)
        # Jala ära löömine
        if plat1_rect.colliderect(tegelase_rect):
            mäng_käib = False

    pg.display.update()
    clock.tick(60)