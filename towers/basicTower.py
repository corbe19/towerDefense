import pygame
from .tower import Tower
import os

class LongRangeTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = []
        self.gun_imgs = []
        self.gun_count = 0

        for x in range(8):
            add_str = str(x)
            if x < 10:
                add_str = "0" + add_str
            self.gun_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Towers/1", "1_" + add_str + ".png")), (64, 64)))

    def draw(self, win):
        super().draw(win)
    
    def attack(self, enemies):
        #attacks enemy, in range, furthest along path

        pass