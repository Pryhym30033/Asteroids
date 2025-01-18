import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_SHOOT_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        return pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    
    def rotate (self, dt):
        self.rotation  += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.rotate(-dt)

        if keys[pygame.K_f]:
            self.rotate(dt)

        if keys[pygame.K_e]:
            self.move(dt)

        if keys[pygame.K_d]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

        self.timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return
        self.timer = SHOOT_COOL_DOWN

        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        shot.velocity += forward * PLAYER_SHOOT_SPEED
