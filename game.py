import pygame

class Game:
    def __init__(self):
        self.running = True
        self.width = 1280
        self.height = 720
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.money = 100
        self.lives = 100
        self.towers = []
        self.bg = pygame.image.load("assets/Background1.png")

    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        
        pygame.quit()