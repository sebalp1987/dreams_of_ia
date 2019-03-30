import pygame
import STRING
import DIALOG
from os import listdir
from utils import animation, input_box, board, cursor, button_check

class CustomScene(object):

    def __init__(self, scene, text):
        self.scene = scene
        print(self.scene)
        self.text = text
        super(CustomScene, self).__init__()

        # Font
        self.font = pygame.font.SysFont("monospace", 18)

        # Images
        dict_scenes = STRING.Images.IMG_DICT
        self.img_names = [f for f in listdir(STRING.Images.PATH_GIF) if f.endswith(dict_scenes.get(self.scene))]
        if len(self.img_names) > 1:
            self.img_names.sort(key=lambda x: int(x[0:2]) if x[1].isdigit() else int(x[0:1]))
            self.images = []
            for img in self.img_names:
                self.images.append(pygame.image.load(STRING.Images.PATH_GIF + img))
                self.anim = animation.Animation(self.images, 0.25)
        else:
            self.img_names = [f for f in listdir(STRING.Images.PATH) if f.endswith(dict_scenes.get(self.scene))]
            self.anim = self.img_names[0]

        # Music
        dict_music = STRING.Sounds.SOUND_DICT
        if dict_music.get(self.scene) is not None:
            pygame.mixer.music.load(STRING.Sounds.PATH + dict_music.get(self.scene))
            pygame.mixer.music.play(1, 0)

        # Text
        dict_text = DIALOG.DICT_TEXT
        self.all_sprites = pygame.sprite.Group()
        b = board.Board()
        c = cursor.Cursor(b)
        self.all_sprites.add(c, b)
        c.write(dict_text.get(self.scene))

        # Button Check
        if STRING.GameParams.DICT_SCENES.get(self.scene) != STRING.GameParams.INPUT_BOX:
            number = 0
            self.press_button = 0
            self.ret_scene = []
            for btn in range(1, len(DIALOG.DICT_BUTTON.get(self.scene)) + 1, 1):
                button = button_check.Button(id=str(self.scene) + str(btn), x=0 + number,
                                             y=STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE * 9 / 10,
                                             width=225, height=50, callback=self.return_scene,
                                             font=pygame.font.SysFont("monospace", 16),
                                             text=DIALOG.DICT_BUTTON.get(self.scene)[btn - 1],
                                             text_color=(255, 255, 255))

                number += 300
                self.all_sprites.add(button)
        # Input Box
        elif STRING.GameParams.DICT_SCENES.get(self.scene) == STRING.GameParams.INPUT_BOX:
            self.input_boxes = [input_box.InputBox(0,
                                                   STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE * 9 / 10, 140, 32)]

    def render(self, screen):
        # Black Fill
        screen.fill((0, 0, 0))

        # Background Image
        if len(self.img_names) == 1:
            image = pygame.transform.scale(pygame.image.load(STRING.Images.PATH + self.anim),
                                           (int(STRING.Maps.MAPWITH * STRING.Maps.TILESIZE / 2),
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
        if len(self.img_names) > 1:
            self.anim.time_interval = 5
            self.anim.update(1)
        self.all_sprites.update()
        pygame.display.update()

    def handle_events(self, e):
        pos = pygame.mouse.get_pos()
        text = None
        if STRING.GameParams.DICT_SCENES.get(self.scene) == STRING.GameParams.INPUT_BOX:
            for box in self.input_boxes:
                text = box.handle_event(e)
        elif STRING.GameParams.DICT_SCENES.get(self.scene) == STRING.GameParams.MENU:
            for btn in self.all_sprites:
                print(btn)
                if type(btn) is button_check.Button:
                    if e.type == pygame.MOUSEBUTTONDOWN and btn.rect.collidepoint(pos):
                        text = 'HOLA'
                        print(text)
                        print(btn.id)
                        self.manager.go_to(CustomScene(scene=str(btn.id)+'-'+str(btn.text), text=btn.text))

        if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN and text is not None:
            self.manager.go_to(CustomScene(scene=self.scene + 1, text=text))

        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            self.manager.go_to(scene=self.scene - 1)

    def return_scene(self):
        return self.press_button

