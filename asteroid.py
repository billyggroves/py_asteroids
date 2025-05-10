import pygame
import circleshape
from constants import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        vect_1 = self.velocity.rotate(angle)
        vect_2 = self.velocity.rotate(-angle)
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = vect_1 * 1.2
        asteroid_2.velocity = vect_2 * 1.2
            
    def update(self, dt):
        self.position += self.velocity * dt