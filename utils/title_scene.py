import pygame
from utils import game_scene, animation, board, cursor
import STRING
import DIALOG
from os import listdir


class TitleScene(object):

    def __init__(self):
        super(TitleScene, self).__init__()
        self.font = pygame.font.SysFont("monospace", 18)
        self.img_names = [f for f in listdir(STRING.Images.PATH) if f.startswith('main.gif-')]
        self.img_names.sort(key=lambda x: int(x[-6:-4]) if x[-6].isdigit() else int(x[-5:-4]))

        self.images = []
        for img in self.img_names:
            self.images.append(pygame.image.load(STRING.Images.PATH + img))
        self.anim = animation.Animation(self.images, 0.25)
        self.all_sprites = pygame.sprite.Group()
        pygame.mixer.music.load(STRING.Sounds.BACKGROUND)
        pygame.mixer.music.play(-1, 0)
        pygame.mouse.set_visible(False)
        b = board.Board()
        c = cursor.Cursor(b)
        c.rect.x = 10
        c.rect.y = 100
        self.all_sprites.add(c, b)
        c.write(DIALOG.TITLE)

    def render(self, screen):
        screen.fill((0, 0, 0))
        image = pygame.transform.scale(self.anim.image, (STRING.Maps.MAPWITH * STRING.Maps.TILESIZE,
                                                 STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE))

        screen.blit(image, (0, 0))
        self.all_sprites.draw(screen)

    def update(self):
        self.anim.time_interval = 2
        self.anim.update(1)
        self.all_sprites.update()
        pygame.display.update()

    def handle_events(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                self.manager.go_to(game_scene.GameScene())
