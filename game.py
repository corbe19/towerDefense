import pygame
import os
from enemies.basic_enemy import Basic_enemy
from enemies.fast_enemy import Fast_enemy
from enemies.strong_enemy import Strong_enemy
from towers.longRangeTower import LongRangeTower, ShortRangeTower

import time
import random

class Game:
    def __init__(self):
        self.running = True
        self.width = 1200
        self.height = 800
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.money = 100
        self.lives = 100
        self.towers = [ShortRangeTower(300, 300), ShortRangeTower(500, 300), ShortRangeTower(700, 300)]
        self.bg = pygame.image.load(os.path.join("game_assets", "Background1.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer = time.time()
       

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            if time.time() - self.timer >= random.randrange(2, 4):
                self.timer = time.time()
                self.enemies.append(random.choice([Basic_enemy(), Fast_enemy(), Strong_enemy()]))
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass


            del_enemy = []       
            for enemy in self.enemies:
                if enemy.x >= 1400:
                    self.lives -= 1
                    del_enemy.append(enemy)
            
            for d in del_enemy:
                self.enemies.remove(d)

            for tower in self.towers:
                tower.attack(self.enemies)
            
            self.draw()
        
        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))

        for enemies in self.enemies:
            enemies.draw(self.win)

        for tower in self.towers:
            tower.draw(self.win)


        pygame.display.update()

g = Game()
g.run()