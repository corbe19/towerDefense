import pygame
import os

class Game:
    def __init__(self):
        self.running = True
        self.width = 1200
        self.height = 800
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.money = 100
        self.lives = 100
        self.towers = []
        self.bg = pygame.image.load(os.path.join("game_assets", "Background1.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
       

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            
            self.draw()
        
        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        pygame.display.update()

g = Game()
g.run()