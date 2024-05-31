import pygame
import os
from enemies.basic_enemy import Basic_enemy
from enemies.fast_enemy import Fast_enemy
from enemies.strong_enemy import Strong_enemy
from towers.longRangeTower import LongRangeTower, ShortRangeTower
from towers.glueTower import GlueTower
pygame.font.init()
import time
import random

lives_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "heart.png")), (32, 32))

class Game:
    def __init__(self):
        self.running = True
        self.width = 1250
        self.height = 800
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.money = 100
        self.lives = 10
        self.towers = [LongRangeTower(300, 300), GlueTower(500, 300), ShortRangeTower(700, 300)]
        self.bg = pygame.image.load(os.path.join("game_assets", "Background1.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer = time.time()
        self.lives_font = pygame.font.SysFont("comicsans", 25)
        self.selected_tower = None

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
                    for tower in self.towers:
                        if tower.click(pos[0], pos[1]):
                            print("clicked")
                            tower.selected = True
                            self.selected_tower = tower
                        else:
                            tower.selected = False


            del_enemy = []       
            for enemy in self.enemies:
                if enemy.x >= 1300:
                    self.lives -= 1
                    del_enemy.append(enemy)
            
            for d in del_enemy:
                self.enemies.remove(d)

            for tower in self.towers:
                tower.attack(self.enemies)

            if self.lives <= 0:
                run = False
            
            self.draw()
        
        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))

        for tower in self.towers:
            tower.draw(self.win)

        for enemies in self.enemies:
            enemies.draw(self.win)

        #draw lives
        text = self.lives_font.render(str(self.lives), 1, (255, 255, 255))
        life = lives_img
        startX = self.width - life.get_width() - 10

        self.win.blit(text, (startX - text.get_width() - 1, 9))

        self.win.blit(life, (startX, 10))


        pygame.display.update()

    def draw_menu(self):
        pass

g = Game()
g.run()