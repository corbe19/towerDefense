import pygame

class Enemy:
    img = []

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = 10
        self.path = [(15, 436), (191, 435), (197, 205), (436, 205), (444, 509), (753, 514), (756, 363), (1178, 356), (1190, 357)]
        self.path_pos = 0
        self.vel = 3

    def draw(self, win):
        # draw enemy
        pass


    def move(self):
        # move enemy
        win.blit(self.img, (self.x, self.y))
        self.move()
        pass

    def collide(self, x, y):
        # check if enemy is hit/range of tower
        if x < self.x + self.width and x > self.x:
            if y > self.y and y < self.y + self.height:
                return True
        pass

    def hit(self):
        # enemy hit

        pass