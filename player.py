import pygame

from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_ACCELERATION, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, direction, dt):
        if direction:
            self.velocity += direction * PLAYER_ACCELERATION * dt
        else:
            self.velocity -= self.velocity * dt
        self.position += self.velocity

    def draw(self, screen):
        color_white = "#ffffff"
        line_width = 2
        pygame.draw.polygon(screen, color_white, self.triangle(), line_width)

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        input_dir = pygame.Vector2(0, self.get_input_axis(pygame.K_s, pygame.K_w)).rotate(self.rotation)
        self.move(input_dir, dt)

        if keys[pygame.K_SPACE] and self.shoot_cooldown <= 0:
            self.shoot()

        self.shoot_cooldown -= dt
    
    def get_input_axis(self, negative_key, positive_key):
        keys = pygame.key.get_pressed()

        if keys[negative_key] == keys[positive_key]:
            return 0
        return 1 if keys[positive_key] else -1