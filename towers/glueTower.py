import pygame
from .tower import Tower
from .longRangeTower import LongRangeTower
import os
import math
import time

gun_imgsG = []
tower_imgsG = []

for i in range(8):
    gun_imgsG.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "G_lvl1", f"frame_{i}_delay-0.1s.gif")), (128, 128)))

tower_imgsG.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "Base", "GlueTowerBase.png")), (90, 90)))

rotated_gun_imgs = gun_imgsG[:]

class GlueTower(LongRangeTower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgsG[:]
        self.gun_imgs = gun_imgsG[:]
        self.gun_count = 0
        self.sell_price = [10, 20, 30]
        self.range = 100
        self.inRange = False
        self.angle = 0
        self.timer = time.time()
        self.damage = 0
        self.fire_rate = .75

        self.rotated_gun_imgs = self.gun_imgs[:]

    def attack(self, enemies):
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x, y = enemy.x, enemy.y
            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos, reverse=True)
        if enemy_closest:
            first_enemy = enemy_closest[0]
            if time.time() - self.timer >= self.fire_rate:
                self.timer = time.time()
                first_enemy.slow()
                       
            self.angle = math.atan2(first_enemy.y - self.y, first_enemy.x - self.x)
            self.angle = math.degrees(self.angle)
            self.rotated_gun_imgs = [pygame.transform.rotate(img, -self.angle - 90) for img in self.gun_imgs]

