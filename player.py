import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)  # Store position as a Vector2
        self.rotation = 0
        self.color = (255, 255, 255)  # White color
        self.shoot_timer = 0  #Creating a timer variable


    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle(), 2)

    # Add these methods to update and access position
    def set_position(self, x, y):
        self.position.x = x
        self.position.y = y

    def get_position(self):
        return self.position.x, self.position.y

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360

 
     

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        #Handle the spacebar (pygame.K_SPACE) and call the shoot method when it is pressed
        if keys[pygame.K_SPACE]:
            self.shoot()

        #Decrease the timer by dt every time update is called on the player
        self.shoot_timer -= dt
        if self.shoot_timer < 0:
            self.shoot_timer = 0


    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):

        if self.shoot_timer <= 0:
            # Create a new shot at the position of the player
            new_shot = Shot(self.position.x, self.position.y)

            # Set the shot's velocity
            new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

            # Reset the timer
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN 

            return new_shot
        # Return None if we can't shoot yet(time)
        return None  
           

