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
    font = pygame.font.SysFont('Consolas', 30)

    counter, text = 1800, '10'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                counter -= 1
                if counter > 0:
                    text = str(counter).rjust(3)
                else:
                    text = font.render("Time Over!!", True, pygame.Color('dodgerblue'))
                    screen.blit(text, (200, 200))
                    pygame.display.flip()
                    screen.fill((20, 20, 20))

            manager.scene.handle_events(event)

        manager.scene.render(screen)
        manager.scene.update()
        screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pygame.display.flip()
        clock.tick(60)



if __name__ == '__main__':
    main()