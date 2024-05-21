import pygame
from .tower import Tower
import os
import math
import time

gun_imgs = []
tower_imgs = []

for i in range(8):
    gun_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "LR_lvl1", f"frame_{i}_delay-0.1s.gif")), (128, 128)))

tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "Base", "LongRangeTowerBase.png")), (96, 96)))

rotated_gun_imgs = gun_imgs[:]  #copy of og gun imgs


class LongRangeTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs[:]
        self.gun_imgs = gun_imgs[:]
        self.gun_count = 0
        self.sell_price = [10, 20, 30]
        self.range = 200
        self.inRange = False
        self.angle = 0
        self.timer = time.time()
        self.damage = 1 

        for i in range(8):
            self.gun_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "LR_lvl1", f"frame_{i}_delay-0.1s.gif")), (128, 128)))

        self.tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "Base", "LongRangeTowerBase.png")), (96, 96)))

        self.rotated_gun_imgs = self.gun_imgs[:]  #copy of og gun imgs

    def draw(self, win):
        super().draw(win)

        # range circle
    #if self.selected:
        surface = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (50, 50, 50, 128), (self.range, self.range), self.range, 0)
        win.blit(surface, (self.x - self.range, self.y - self.range))

        # only animate if enemy in range
        if self.inRange:
            self.gun_count += 1
            if self.gun_count >= len(self.gun_imgs) * 5:
                self.gun_count = 0
        else:
            self.gun_count = 0

        gun = self.rotated_gun_imgs[self.gun_count // 5]
        win.blit(gun, ((self.x + self.width / 2) - (gun.get_width() / 2), (self.y - gun.get_height() / 2)))

    def change_range(self, r):
        # change range
        self.range = r

    def attack(self, enemies):
        # attacks enemy, in range, furthest along path
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x, y = enemy.x, enemy.y
            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos, reverse=True)
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if time.time() - self.timer >= .75:
                self.timer = time.time()
                if first_enemy.hit() == True:
                    enemies.remove(first_enemy)

            # Calculate the angle to the enemy
            self.angle = math.atan2(first_enemy.y - self.y, first_enemy.x - self.x)
            self.angle = math.degrees(self.angle)

            # Rotate gun images
            self.rotated_gun_imgs = [pygame.transform.rotate(img, -self.angle - 90) for img in self.gun_imgs]


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

        for i in range(8):
            self.gun_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "SR_lvl1", f"frame_{i}_delay-0.1s.gif")), (128, 128)))

        self.tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "Base", "ShortRangeTowerBase.png")), (96, 96)))

        self.rotated_gun_imgs = self.gun_imgs[:]
        
