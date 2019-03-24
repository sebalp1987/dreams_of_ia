from utils import scene, input_box, second_scene
import pygame
import STRING


class GameScene(scene.Scene):
    def __init__(self):
        super(GameScene, self).__init__()
        self.font = pygame.font.SysFont("monospace", 18)
        self.sfont = pygame.font.SysFont('Arial', 32)
        self.background = pygame.image.load(STRING.Images.COVER)
        self.input_boxes = [input_box.InputBox(0,
                                               STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE * 9 / 10, 140, 32)]
        pygame.mouse.set_visible(True)

    def render(self, screen):
        background = pygame.transform.scale(self.background, (STRING.Maps.MAPWITH * STRING.Maps.TILESIZE,
                                                              STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE))

        textsurface = self.font.render('¿Cuál es tu nombre?', False, STRING.Colors.MONO)
        screen.blit(background, (0, 0))

        pygame.draw.rect(screen, STRING.Colors.BLACK, (0,
                                                       STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE * 4 / 5,
                                                       STRING.Maps.MAPWITH * STRING.Maps.TILESIZE,
                                                       STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE / 5))
        screen.blit(textsurface, (0,
                                  STRING.Maps.MAPHEIGHT * STRING.Maps.TILESIZE * 4 / 5))

        for box in self.input_boxes:
            box.draw(screen)

    def update(self):
        for box in self.input_boxes:
            box.update()

    def handle_events(self, e):
        for box in self.input_boxes:
            box.handle_event(e)
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            self.manager.go_to(second_scene.CustomScene(0))

        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            pass  # somehow go back to menu
