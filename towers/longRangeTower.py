import pygame
from .tower import Tower
import os

class LongRangeTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = []
        self.gun_imgs = []
        self.gun_count = 0
        self.sell_price = [10, 20, 30]

        for x in range(8):
            self.gun_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets\Towers\LR_lvl1", "frame_" + str(x) + "_delay-0.1s.gif")), (128, 128)))

        self.tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets\Towers\Base", "LongRangeTowerBase.png")), (128, 128)))

    def draw(self, win):
        super().draw(win)
        if self.gun_count >= len(self.gun_imgs):
            self.gun_count = 0

        gun = self.gun_imgs[self.gun_count]
        win.blit(gun, ((self.x + self.width/2) - (gun.get_width()/2), (self.y - gun.get_height()/2)))
        self.gun_count += 1

    def attack(self, enemies):
        #attacks enemy, in range, furthest along path

        pass