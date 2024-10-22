import pygame
import sys

from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    BLACK = (0, 0, 0)
    running = True
   

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #setting containers for the Shot class
    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroid_group, updatable, drawable)

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

        # Check for new shots (not needed as in group updatable)
        #new_shot = player.shoot()
    

        for asteroid in asteroid_group:

            # Check for collisions between player and asteroid
            if asteroid.check_collision(player):
                sys.exit("Game Over!")

        # Check for collisions between asteroids and shots
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()
                    
                    


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





 