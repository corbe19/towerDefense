import pygame
import os
from .enemy import Enemy

class Basic_enemy(Enemy):
    def __init__(self):
        super().__init__()
        self.vel = 3
        self.img = (pygame.transform.scale(pygame.image.load(os.path.join("game_assets\Enemies", "enemy1.png")), (64, 64)))