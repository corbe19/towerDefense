import pygame
from .tower import Tower
from .longRangeTower import LongRangeTower
import os
import math
import time

gun_imgsSR = []
tower_imgsSR = []

for i in range(8):
    gun_imgsSR.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "SR_lvl1", f"frame_{i}_delay-0.1s.gif")), (128, 128)))

tower_imgsSR.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "Base", "ShortRangeTowerBase.png")), (96, 96)))

rotated_gun_imgs = gun_imgsSR[:]


class ShortRangeTower(LongRangeTower):
    def __intit__(self,x,y):
        super().__init__(x,y)
        self.tower_imgs = tower_imgsSR[:]
        self.gun_imgs = gun_imgsSR[:]
        self.gun_count = 0
        self.sell_price = [10, 20, 30]
        self.range = 100
        self.inRange = False
        self.angle = 0
        self.timer = time.time()
        self.damage = 1 
        self.fire_rate = 1.5

        for i in range(8):
            self.gun_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "SR_lvl1", f"frame_{i}_delay-0.1s.gif")), (128, 128)))

        self.tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "Base", "ShortRangeTowerBase.png")), (96, 96)))

        self.rotated_gun_imgs = self.gun_imgs[:]