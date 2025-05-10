from constants import *
import pygame
from player import *

def main():
    pygame.init()
    
    fpsClock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print(player)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, "black")
        
        player.update(dt)
        player.draw(screen)

        pygame.display.flip()
        dt = fpsClock.tick(60) / 1000

        

if __name__ == "__main__":
    main()
