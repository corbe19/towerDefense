import pygame
import os
from .enemy import Enemy

class Fast_enemy(Enemy):
    def __init__(self):
        super().__init__()
        self.vel = 6
        self.max_health = 2
        self.health = self.max_health
        self.img = (pygame.transform.scale(pygame.image.load(os.path.join("game_assets\Enemies", "enemy3.png")), (64, 64)))