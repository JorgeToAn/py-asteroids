import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        color_white = "#ffffff"
        width = 2
        pygame.draw.circle(screen, color_white, self.position, self.radius, width)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius == ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        vectors = (self.velocity.rotate(random_angle), self.velocity.rotate(-random_angle))
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        for i, v in enumerate(vectors):
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = vectors[i] * 1.2
