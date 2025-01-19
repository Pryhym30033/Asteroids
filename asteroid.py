import pygame
from constants import *
import random


from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position.x = x
        self.position.y = y
        self.radius = radius



    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        randomAngle = random.uniform(20, 50)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            velocity1 = self.velocity.rotate(randomAngle)
            velocity2 = self.velocity.rotate(-randomAngle)
            astro1 = Asteroid(self.position.x, self.position.y, newRadius)
            astro2 = Asteroid(self.position.x, self.position.y, newRadius)
            astro1.velocity = velocity1 * 1.2
            astro2.velocity = velocity2 * 1.2
        
