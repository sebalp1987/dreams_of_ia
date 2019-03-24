import pygame
import STRING
import DIALOG
from os import listdir
from utils import animation, input_box, board, cursor


class CustomScene(object):

    def __init__(self, scene, text):
        self.scene = scene
        self.text = text
        super(CustomScene, self).__init__()

        # Font
        self.font = pygame.font.SysFont("monospace", 18)

        # Images
        dict_scenes = STRING.Images.IMG_DICT
        self.img_names = [f for f in listdir(STRING.Images.PATH) if f.startswith(dict_scenes.get(self.scene))]
        self.images = []
        for img in self.img_names:
            self.images.append(pygame.image.load(STRING.Images.PATH + img))
        if len(self.images) > 1:
                self.anim = animation.Animation(self.images, 0.25)
        else:
            self.anim = self.images[0]

        # Music
        dict_music = STRING.Sounds.SOUND_DICT
        pygame.mixer.music.load(STRING.Sounds.PATH + dict_music.get(self.scene))
        pygame.mixer.music.play(-1, 0)

        # Input Box
        self.input_boxes = [input_box.InputBox(0,
                                               STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE * 9 / 10, 140, 32)]

        # Text
        dict_text = DIALOG.DICT_TEXT
        self.all_sprites = pygame.sprite.Group()
        b = board.Board()
        c = cursor.Cursor(b)
        self.all_sprites.add(c, b)
        c.write(dict_text.get(self.scene))

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
        textsurface = self.font.render(DIALOG.DICT_TEXT_DOWN.get(self.scene), False, STRING.Colors.MONO)
        screen.blit(textsurface, (0, STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE * 8 / 10))

        # Text Left
        self.all_sprites.draw(screen)

        # Input Box
        for box in self.input_boxes:
            box.draw(screen)

    def update(self):
        self.anim.update(60)
        self.all_sprites.update()
        pygame.display.update()

    def handle_events(self, e):
        text = None
        for box in self.input_boxes:
            text = box.handle_event(e)

        if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN and text is not None:
            self.manager.go_to(CustomScene(scene=self.scene + 1, text=text))

        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            self.manager.go_to(scene=self.scene - 1)