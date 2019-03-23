import os
import pygame as pg
LOCAL = os.path.dirname(os.path.abspath(__file__))


class GameParams:

    name = 'Dreams of IA'

class Colors:
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    SILVER = (192, 192, 192)
    COLOR_INACTIVE = pg.Color('lightskyblue3')
    COLOR_ACTIVE = pg.Color('dodgerblue2')

class Maps:
    TILESIZE = 100
    MAPWITH = 5
    MAPHEIGHT = 3


class Images:
    COVER = LOCAL + '/resource/image/cover.jpg'

class Sounds:
    BACKGROUND = LOCAL + '/resource/sound/background.mp3'