import pygame as pg


pg.init() #paneb pygame'i tööle

screen = pg.display.set_mode((1200, 600))
color = (255, 0, 0)
x = 0
pg.draw.rect(screen, color, pg.Rect(x, 30, 60, 60))
pg.display.update()

class ruut:
    def __init__(self, kylePikkus):
        self.kyljePikkus = kylePikkus



xKordinaat = 1


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break

    if x == 1200:
        x =0

    pg.time.delay(10) #et pilti aeglustada
    screen.fill((0, 0, 0)) #tagumise ekraani pilt
    pg.draw.rect(screen, (0, 255, 0), (xKordinaat, 30, 60, 60))# kuhu, värv(r,g,b), (asukoht x, asukoht y, kui suur x, kui suur y)

    pg.display.update()#joonistab uue pildi, teed pildi valmis ja siis tuleb update()
    x += 1


