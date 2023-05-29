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

# Mängu seis, 0-avamenüü; 1-mäng; 2-väljumine
mangu_seis = 0


# Tausta ja muu import
x = 200
y = 470
background_image = pygame.image.load("taust.png")
tegelase_image_vasak = pg.image.load("Nimetu_vasak.png")
tegelase_image_vasak_rect = tegelase_image_vasak.get_rect(bottomleft = (x, y))
tegelase_image_parem = pg.image.load("Nimetu_parem.png")
tegelase_image_parem_rect = tegelase_image_parem.get_rect(bottomleft = (x, y))


# Ruudu koordinaadid
suund = "parem"


#Tegelane
tegelane = pg.Surface((30,30))
tegelane.fill((255,0,0))


#Platvorm
plat_surf = pg.Surface((100, 20))
plat_rect = plat_surf.get_rect(bottomleft = (100, 500))


#Punktid
punktid = 0
test_font = pg.font.Font(None, 30)
text_surface = test_font.render(f'Punkte {punktid}', True, (0,0,0))

#Gravitatsioon
gravitatsioon = 0

# Taimer
aeg = 0
AegList = [0]

# Mängu lõppnupp
lõppnupp_surf = pg.image.load("Lõpuekraan.png")


while True:
    # Käskude kordumine
    pg.time.delay(10)


    # Klaviatuuri käsud
    for event in pg.event.get():
        #Väljumine
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    #hüpe
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_UP:
            gravitatsioon = -15
    #paremale-vasakule
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_RIGHT:
            suund = "parem"
            tegelase_image_parem_rect.x += 10
            tegelase_image_vasak_rect.x += 10
        if event.key == pg.K_LEFT:
            suund = "vasak"
            tegelase_image_parem_rect.x -= 10
            tegelase_image_vasak_rect.x -= 10
    # Hiir
    if event.type == pg.MOUSEBUTTONDOWN:
        if start_nupp_rect.collidepoint(event.pos):
            mangu_seis = 1
        if valju_nupp_rect.collidepoint(event.pos):
            mangu_seis = 2


    # Gravitatsiooni muut
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


    #Kokkupõrge
    if tegelase_image_parem_rect.colliderect(plat_rect):
        punktid += 1
        plat_rect.bottomleft = (randint(0, 700), randint(0, 550))
        #Platvorm, mida püütakse muudab iga kord suurust
        plat_surf = pg.Surface((randint(10,100), randint(10,100)))


    if mangu_seis == 0:
        # Avamenüü nupud
        start_nupp_surf = pg.image.load("start_nupp.png")
        start_nupp_rect = start_nupp_surf.get_rect(center=(400, 200))
        valju_nupp_surf = pg.image.load("välju_nupp.png")
        valju_nupp_rect = valju_nupp_surf.get_rect(center=(400, 400))
        # Avamenüü joonistamine
        screen.blit(background_image, (0,0))
        screen.blit(start_nupp_surf, start_nupp_rect)
        screen.blit(valju_nupp_surf, valju_nupp_rect)
    elif mangu_seis == 1:
        # Käiva mängu joonistamine
        screen.blit(background_image, (0, 0))
        #aja lugemine algab, kui vajutada start nuppu
        aeg = pg.time.get_ticks()
            # Tegelase suund
        if suund == "parem":
            screen.blit(tegelase_image_parem, tegelase_image_parem_rect)
        elif suund == "vasak":
            screen.blit(tegelase_image_vasak, tegelase_image_vasak_rect)
            # Platvorm
        screen.blit(plat_surf, plat_rect)

        #Punktide näitamine
        text_surface = test_font.render(f'Punkte: {punktid}', True, (0,0,0))
        screen.blit(text_surface, (100, 50))
    else:
        pg.quit()
        exit()

    #Taimer
    if aeg == 0:
        print()
    else:
        AegList.append(aeg)
        if aeg - AegList[1] > 30000:
            screen.blit(lõppnupp_surf, (0, 0))
            text_surface = test_font.render(f'Punkte mängust: {punktid}', True, (0, 0, 0))
            screen.blit(text_surface, (300, 350))

    pg.display.update()
    clock.tick(60)


