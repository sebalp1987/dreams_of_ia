import pygame
import sys
import STRING

from utils import scene_manager
from pygame.locals import *

def main():
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((STRING.Maps.MAPWITH*STRING.Maps.TILESIZE,
                                           STRING.Maps.MAPHEIGHT*STRING.Maps.TILESIZE))
    pygame.display.set_caption(STRING.GameParams.name)
    manager = scene_manager.SceneMananger()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            manager.scene.handle_events(event)
        manager.scene.render(screen)
        manager.scene.update()
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()