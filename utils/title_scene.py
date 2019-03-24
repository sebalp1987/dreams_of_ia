import pygame
from utils import game_scene, input_box, animation, board, cursor
import STRING
from os import listdir

class TitleScene(object):

    def __init__(self):
        super(TitleScene, self).__init__()
        self.font = pygame.font.SysFont('Comic Sans MS', 18)
        self.img_names = [f for f in listdir(STRING.Images.PATH) if f.startswith('main.gif-')]
        self.images = []
        for img in self.img_names:
            self.images.append(pygame.image.load(STRING.Images.PATH + img))
        self.anim = animation.Animation(self.images, 0.25)
        self.all_sprites = pygame.sprite.Group()

        pygame.mixer.init()
        pygame.mixer.music.load(STRING.Sounds.BACKGROUND)
        pygame.mixer.music.play(-1, 0)
        pygame.mouse.set_visible(False)
        b = board.Board()
        c = cursor.Cursor(b)
        self.all_sprites.add(c, b)
        c.write("""Welcome to Dreams of IA...
        Press Enter... if you dare"""
            )

    def render(self, screen):
        screen.fill((0, 0, 0))
        image = pygame.transform.scale(self.anim.image, (STRING.Maps.MAPWITH * STRING.Maps.TILESIZE,
                                                 STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE))

        screen.blit(image, (0, 0))
        self.all_sprites.draw(screen)

    def update(self):
        self.anim.update(60)
        self.all_sprites.update()
        pygame.display.update()

    def handle_events(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                self.manager.go_to(game_scene.GameScene())
