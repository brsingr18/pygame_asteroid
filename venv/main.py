import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    BLACK = (0, 0, 0)
    running = True
   

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()

    Asteroid.containers = (asteroid, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # Create player and add to groups
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    dt = 0


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for obj in updatable:
            obj.update(dt)

      # Clear the screen
        screen.fill(BLACK)

        for obj in drawable:
            obj.draw(screen)

        # Get the time elapsed since the last frame, framerate 60 FPS
        dt = clock.tick(60) / 1000


        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()





 