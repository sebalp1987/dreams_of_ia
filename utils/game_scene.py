from utils import scene, input_box, custom_scene, board, cursor, title_scene
import pygame
import STRING
import DIALOG


class GameScene(scene.Scene):
    def __init__(self):
        super(GameScene, self).__init__()
        self.font = pygame.font.SysFont("monospace", 18)
        self.background = pygame.image.load(STRING.Images.COVER)
        self.input_boxes = [input_box.InputBox(0,
                                               STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE * 9 / 10, 140, 32)]
        self.all_sprites = pygame.sprite.Group()

        pygame.mouse.set_visible(True)
        b = board.Board()
        c = cursor.Cursor(b)
        self.all_sprites.add(c, b)
        c.write(DIALOG.GAME_SCENE)

    def render(self, screen):
        # Black Fill
        screen.fill((0, 0, 0))

        # Background Image
        background = pygame.transform.scale(self.background, (int(STRING.Maps.MAPWITH * STRING.Maps.TILESIZE / 2),
                                                              STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE))

        screen.blit(background, (int(STRING.Maps.MAPWITH * STRING.Maps.TILESIZE / 2), 0))

        # Text Rectangle
        pygame.draw.rect(screen, STRING.Colors.BLACK, (0,
                                                       STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE * 4 / 5,
                                                       STRING.Maps.MAPWITH * STRING.Maps.TILESIZE,
                                                       STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE / 5))

        # Text Down
        textsurface = self.font.render(DIALOG.GAME_SCENE_1, False, STRING.Colors.MONO)
        screen.blit(textsurface, (0, STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE * 8 / 10))

        # Text Left
        self.all_sprites.draw(screen)

        # Input Box
        for box in self.input_boxes:
            box.draw(screen)

    def update(self):
        for box in self.input_boxes:
            box.update()
        self.all_sprites.update()
        pygame.display.update()

    def handle_events(self, e):
        text = None
        for box in self.input_boxes:
            text = box.handle_event(e)

        if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN and text is not None:
            self.manager.go_to(custom_scene.CustomScene(scene=0, text=text))

        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            self.manager.go_to(title_scene.TitleScene())
