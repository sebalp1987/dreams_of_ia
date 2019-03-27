import os
import pygame as pg
LOCAL = os.path.dirname(os.path.abspath(__file__))


class GameParams:

    name = 'Dreams of IA'
    FPS = 60
    INPUT_BOX = 0
    MENU = 3
    DICT_SCENES = {0: MENU}

class Colors:
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    SILVER = (192, 192, 192)
    MONO = (255, 255, 0)
    COLOR_INACTIVE = BLUE
    COLOR_ACTIVE = pg.Color('dodgerblue2')

class Maps:
    TILESIZE = 100
    MAPWITH = 9
    MAPHEIGHT = 7


class Images:
    PATH = LOCAL + '/resource/image/'
    COVER = LOCAL + '/resource/image/cover.jpg'
    MAIN = LOCAL + '/resource/image/main.gif'
    CITY = LOCAL + '/resource/image/city.gif'
    IMG_DICT = {0: 'city.gif'}

class Sounds:
    BACKGROUND = LOCAL + '/resource/sound/background.mp3'
    PATH = LOCAL + '/resource/sound/'
    SOUND_DICT = {0: None}
