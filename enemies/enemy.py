import pygame
import math

class Enemy:
    img = []

    def __init__(self):
        self.width = 64
        self.height = 64
        self.health = 10
        self.img = None
        self.path = [(15, 436), (191, 435), (197, 205), (436, 205), (444, 509), (753, 514), (756, 363), (1178, 356), (1190, 357)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.path_pos = 0
        self.vel = .25
        self.move_count = 0
        self.move_dis = 0
        self.dis = 0

    def draw(self, win):
        # draw enemy
        win.blit(self.img, (self.x, self.y))
        self.move()


    def move(self):
        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (1190, 357)
        else:
            x2, y2 = self.path[self.path_pos + 1]

        move_dis = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        self.move_count += 1
        dirvect = (x2 - x1, y2 - y1)

        move_x, move_y = (self.x + dirvect[0] * self.move_count, self.y + dirvect[1] * self.move_count)
        self.dis += math.sqrt((move_x - x1)**2 + (move_y - y1)**2)

        #next path point
        if self.dis >= move_dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1

        self.x = move_x
        self.y = move_y




    def collide(self, x, y):
        # check if enemy is hit/range of tower
        if x < self.x + self.width and x > self.x:
            if y > self.y and y < self.y + self.height:
                return True
        return False

    def hit(self):
        # enemy hit

        pass