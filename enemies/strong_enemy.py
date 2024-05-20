import pygame
import os
from .enemy import Enemy

class Strong_enemy(Enemy):
    def __init__(self):
        super().__init__()
        self.vel = 1
        self.max_health = 7
        self.health = self.max_health
        self.img = (pygame.transform.scale(pygame.image.load(os.path.join("game_assets\Enemies", "enemy4.png")), (64, 64)))