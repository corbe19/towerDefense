import pygame
import os
from enemies.basic_enemy import Basic_enemy
from enemies.fast_enemy import Fast_enemy
from enemies.strong_enemy import Strong_enemy

class Game:
    def __init__(self):
        self.running = True
        self.width = 1200
        self.height = 800
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = [Basic_enemy()]
        self.money = 100
        self.lives = 100
        self.towers = []
        self.bg = pygame.image.load(os.path.join("game_assets", "Background1.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
       

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            pygame.time.delay(500)
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            for enemy in self.enemies:
                if enemy.x == enemy.path[-1][0]:
                    self.lives -= 1
                    self.enemies.remove(enemy)
            
            self.draw()
        
        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        for enemies in self.enemies:
            enemies.draw(self.win)
        pygame.display.update()

g = Game()
g.run()