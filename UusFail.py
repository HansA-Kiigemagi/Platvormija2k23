import pygame as pg

pg.init()

screen = pg.display.set_mode((1280, 480))
pg.display.set_caption("Mäng") #akna pealkiri
pg.mouse.set_visible(False)


background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((178, 0, 178))

if pg.font:
    font = pg.font.Font(None, 32)
    text = font.render("See text läheb ekraanile", True, (10, 10, 10))
    textpos = text.get_rect(centerx=background.get_width() /2, y = 10)
    background.blit(text, textpos)

screen.blit(background, (0, 0))
pg.display.flip()


#clock = pg.time.Clock()

going = True
while going:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            going = False

pg.quit()