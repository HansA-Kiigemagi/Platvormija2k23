import pygame as pg
from sys import exit

import pygame.image

pg.init()

screen = pg.display.set_mode((800,600))
pg.display.set_caption("Mäng")
clock = pg.time.Clock()

surface = pg.Surface((300,300))
surface.fill("blue")

background_image = pygame.image.load("taust.png")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.blit(background_image, (0,0))
    screen.blit(surface, (200, 100))

    pg.display.update()
    clock.tick(60)