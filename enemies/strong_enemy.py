import pygame
import os
from .enemy import Enemy

class Strong_enemy(Enemy):
    def __init__(self):
        super().__init__()
        self.img = (pygame.transform.scale(pygame.image.load(os.path.join("game_assets\Enemies", "enemy4.png")), (64, 64)))