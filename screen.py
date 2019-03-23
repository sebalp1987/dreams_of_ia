import pygame
import sys
import STRING

from utils import input_box
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(STRING.Sounds.BACKGROUND)
pygame.mixer.music.play(-1, 0)

DISPLAYSURF = pygame.display.set_mode((STRING.Maps.MAPWITH*STRING.Maps.TILESIZE,
                                       STRING.Maps.MAPHEIGHT*STRING.Maps.TILESIZE))
pygame.display.set_caption(STRING.GameParams.name)
background = pygame.image.load(STRING.Images.COVER)
background = pygame.transform.scale(background,(STRING.Maps.MAPWITH*STRING.Maps.TILESIZE,
                                       STRING.Maps.MAPHEIGHT*STRING.Maps.TILESIZE))
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('¿Cuál es tu nombre?', False, STRING.Colors.SILVER)
input_box1 = input_box.InputBox(100, 100, 140, 32)
input_box2 = input_box.InputBox(100, 300, 140, 32)
input_boxes = [input_box1, input_box2]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        for box in input_boxes:
            box.handle_event(event)

    DISPLAYSURF.blit(background, (0, 0))
    DISPLAYSURF.blit(textsurface, (100, 250))
    for box in input_boxes:
        box.update()

    for box in input_boxes:
        box.draw(DISPLAYSURF)
    # pygame.draw.rect(DISPLAYSURF, (0, 250, 0), (100, 50, 20, 20)) # Color, (x, y, weight, height)
    pygame.display.update()

