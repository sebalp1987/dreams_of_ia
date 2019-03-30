import os
import pygame as pg
LOCAL = os.path.dirname(os.path.abspath(__file__))


class GameParams:

    name = 'Dreams of IA'
    FPS = 60
    INPUT_BOX = 0
    MENU = 3
    DICT_SCENES = {0: MENU, '01-Ir a la Ciudad': MENU, '01-Preguntar Direcciones': MENU}

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
    PATH_GIF = LOCAL + '/resource/image/gif/'
    COVER = LOCAL + '/resource/image/cover.jpg'
    MAIN = LOCAL + '/resource/image/main.gif'
    CITY = LOCAL + '/resource/image/city.gif'
    IMG_DICT = {0: 'city.gif', '01-Preguntar Direcciones': 'giphy.png',
                                '01-Preguntar Direcciones1-AI-3000': 'ai3000.gif',
                                '01-Preguntar Direcciones2-Robots': 'robots.gif',
                                '01-Preguntar Direcciones3-Humanos': 'apocalipsis.png'
                }


class Sounds:
    BACKGROUND = LOCAL + '/resource/sound/background.mp3'
    PATH = LOCAL + '/resource/sound/'
    SOUND_DICT = {0: None, '01-Preguntar Direcciones': 'help_you.wav',
                  '01-Preguntar Direcciones1-AI-3000': 'binary.wav',
                  '01-Preguntar Direcciones2-Robots': None,
                  '01-Preguntar Direcciones3-Humanos': None
                  }
