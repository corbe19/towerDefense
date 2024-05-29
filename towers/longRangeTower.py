import pygame
from .tower import Tower
import os
import math
import time

# Load images outside the classes to avoid redundant loading
gun_imgs = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "LR_lvl1", f"frame_{i}_delay-0.1s.gif")), (128, 128)) for i in range(8)]
tower_base_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "Base", "LongRangeTowerBase.png")), (96, 96))

gun_imgsSR = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "SR_lvl1", f"frame_{i}_delay-0.1s.gif")), (128, 128)) for i in range(8)]
tower_base_imgSR = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "Towers", "Base", "ShortRangeTowerBase.png")), (96, 96))


class LongRangeTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = [tower_base_img]
        self.gun_imgs = gun_imgs[:]
        self.gun_count = 0
        self.sell_price = [10, 20, 30]
        self.range = 200
        self.inRange = False
        self.angle = 0
        self.timer = time.time()
        self.damage = 1 
        self.fire_rate = .75
        self.animation_speed = 5
        self.rotated_gun_imgs = self.gun_imgs[:]

    def draw(self, win):
        super().draw(win)
        surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (50, 50, 50, 128), (self.range, self.range), self.range, 0)
        win.blit(surface, (self.x - self.range, self.y - self.range))

        if self.inRange:
            self.gun_count += 1
            if self.gun_count >= len(self.gun_imgs) * self.animation_speed:
                self.gun_count = 0
        else:
            self.gun_count = 0

        gun = self.rotated_gun_imgs[self.gun_count // self.animation_speed]
        win.blit(gun, ((self.x + self.width / 2) - (gun.get_width() / 2), (self.y - gun.get_height() / 2)))

    def change_range(self, r):
        self.range = r

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
                if first_enemy.hit():
                    enemies.remove(first_enemy)

            self.angle = math.atan2(first_enemy.y - self.y, first_enemy.x - self.x)
            self.angle = math.degrees(self.angle)
            self.rotated_gun_imgs = [pygame.transform.rotate(img, -self.angle - 90) for img in self.gun_imgs]


class ShortRangeTower(LongRangeTower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = [tower_base_imgSR]
        self.gun_imgs = gun_imgsSR[:]
        self.range = 125
        self.fire_rate = .3
        self.animation_speed = 2
        self.rotated_gun_imgs = self.gun_imgs[:]

        
