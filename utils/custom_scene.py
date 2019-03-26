import pygame
import STRING
import DIALOG
from os import listdir
from utils import animation, input_box, board, cursor, button_check

class CustomScene(object):

    def __init__(self, scene, text):
        self.scene = scene
        self.text = text
        super(CustomScene, self).__init__()

        # Font
        self.font = pygame.font.SysFont("monospace", 18)

        # Images
        dict_scenes = STRING.Images.IMG_DICT
        self.img_names = [f for f in listdir(STRING.Images.PATH) if f.endswith(dict_scenes.get(self.scene))]
        self.img_names.sort(key=lambda x: int(x[0:2]) if x[1].isdigit() else int(x[0:1]))
        self.images = []
        for img in self.img_names:
            self.images.append(pygame.image.load(STRING.Images.PATH + img))
        if len(self.images) > 1:
            self.anim = animation.Animation(self.images, 0.25)
        else:
            self.anim = self.images[0]

        # Music
        dict_music = STRING.Sounds.SOUND_DICT
        if dict_music.get(self.scene) is not None:
            pygame.mixer.music.load(STRING.Sounds.PATH + dict_music.get(self.scene))
            pygame.mixer.music.play(-1, 0)

        # Text
        dict_text = DIALOG.DICT_TEXT
        self.all_sprites = pygame.sprite.Group()
        b = board.Board()
        c = cursor.Cursor(b)
        self.all_sprites.add(c, b)
        c.write(dict_text.get(self.scene))

        # Input Box
        if STRING.GameParams.DICT_SCENES.get(self.scene) != STRING.GameParams.INPUT_BOX:
            self.number = 0
            for btn in range(1, STRING.GameParams.MENU + 1, 1):
                self.button = button_check.Button(320, 70, 170, 65, self.return_value,
                              self.font, 'Increment', (255, 255, 255))
            self.all_sprites.add(self.button)

        elif STRING.GameParams.DICT_SCENES.get(self.scene) == STRING.GameParams.INPUT_BOX:
            self.input_boxes = [input_box.InputBox(0,
                                                   STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE * 9 / 10, 140, 32)]


    def render(self, screen):
        # Black Fill
        screen.fill((0, 0, 0))

        # Background Image
        if len(self.images) == 1:
            image = pygame.transform.scale(self.anim, (STRING.Maps.MAPWITH * STRING.Maps.TILESIZE,
                                                       STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE))
        else:
            image = pygame.transform.scale(self.anim.image, (STRING.Maps.MAPWITH * STRING.Maps.TILESIZE,
                                                             STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE))

        screen.blit(image, (int(STRING.Maps.MAPWITH * STRING.Maps.TILESIZE / 2), 0))

        # Text Rectangle
        pygame.draw.rect(screen, STRING.Colors.BLACK, (0,
                                                       STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE * 4 / 5,
                                                       STRING.Maps.MAPWITH * STRING.Maps.TILESIZE,
                                                       STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE / 5))

        # Text Down
        textsurface = self.font.render(DIALOG.DICT_TEXT_DOWN.get(self.scene).format(self.text), False,
                                       STRING.Colors.MONO)
        screen.blit(textsurface, (0, STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE * 8 / 10))

        # Text Left
        self.all_sprites.draw(screen)

        # Input Box
        if STRING.GameParams.DICT_SCENES.get(self.scene) == STRING.GameParams.INPUT_BOX:
            for box in self.input_boxes:
                box.draw(screen)

    def update(self):
        self.anim.time_interval = 5
        self.anim.update(1)
        self.all_sprites.update()
        pygame.display.update()

    def handle_events(self, e):
        text = None
        if STRING.GameParams.DICT_SCENES.get(self.scene) == STRING.GameParams.INPUT_BOX:
            for box in self.input_boxes:
                text = box.handle_event(e)
        elif STRING.GameParams.DICT_SCENES.get(self.scene) == STRING.GameParams.MENU:
            for btn in self.all_sprites:
                if type(btn) is button_check.Button:
                    btn.handle_event(e)

        if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN and text is not None:
            self.manager.go_to(CustomScene(scene=self.scene + 1, text=text))

        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            self.manager.go_to(scene=self.scene - 1)

    def return_value(self):
        self.number += 1
        print(self.number)