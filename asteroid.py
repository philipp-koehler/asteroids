from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(x, y, radius)
    
    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        asteroid1_angle = self.velocity.rotate(angle)
        asteroid2_angle = self.velocity.rotate(-angle)
        asteroid1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        asteroid2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        asteroid1.velocity = asteroid1_angle * 1.2
        asteroid2.velocity = asteroid2_angle * 1.2
        

    def draw(self, screen):
        pygame.draw.circle(screen, center=self.position, radius=self.radius, width=2, color="white")
    
    def update(self, dt):
        self.position += self.velocity * dt

