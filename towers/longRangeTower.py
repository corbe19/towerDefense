import pygame
from .tower import Tower
import os
import math

class LongRangeTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = []
        self.gun_imgs = []
        self.gun_count = 0
        self.sell_price = [10, 20, 30]
        self.range = 200
        self.inRange = False
        self.angle = 0

        for x in range(8):
            self.gun_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets\Towers\LR_lvl1", "frame_" + str(x) + "_delay-0.1s.gif")), (128, 128)))

        self.tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets\Towers\Base", "LongRangeTowerBase.png")), (96, 96)))

    def draw(self, win):
        super().draw(win)

        #range circle
        if self.selected:
            surface = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (50,50,50, 128), (self.range, self.range), self.range, 0)

            win.blit(surface, (self.x - self.range, self.y - self.range))
        
        #only animate if enemy in range
        if self.inRange:
            self.gun_count += 1
            if self.gun_count >= len(self.gun_imgs)*5:
                self.gun_count = 0
        else:
            self.gun_count = 0

        gun = self.gun_imgs[self.gun_count//5]
        win.blit(gun, ((self.x + self.width/2) - (gun.get_width()/2), (self.y - gun.get_height()/2)))


    def change_range(self, r):
        #change range
        self.range = r

    def attack(self, enemies):
        #attacks enemy, in range, furthest along path
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x, y = enemy.x, enemy.y
            dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos, reverse=True)
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]

            for x, img in enumerate(self.gun_imgs):
                self.angle = 0
                self.angle = math.degrees(math.atan(((self.y - first_enemy.y) / (self.x - first_enemy.x))))
                self.gun_imgs[x] = pygame.transform.rotate(img, self.angle)


        
