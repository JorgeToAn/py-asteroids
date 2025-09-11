import pygame

import circleshape

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        color_white = "#ffffff"
        width = 2
        pygame.draw.circle(screen, color_white, self.position, self.radius, width)
    
    def update(self, dt):
        self.position += self.velocity * dt
