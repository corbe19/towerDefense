import pygame
import math

class Enemy:
    img = []

    def __init__(self):
        self.width = 64
        self.height = 64
        self.health = 10
        self.img = None
        self.path = [(-70, 436), (15, 436), (191, 435), (197, 205), (436, 205), (444, 509), (753, 514), (756, 363), (1178, 356), (1190, 357), (1400, 357), (1470, 357)]
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
            x2, y2 = (-10, 355)
        else:
            x2, y2 = self.path[self.path_pos+1]

        dirn = ((x2-x1)*2, (y2-y1)*2)
        length = math.sqrt((dirn[0])**2 + (dirn[1])**2)
        dirn = (dirn[0]/length, dirn[1]/length)

        move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1]))

        self.x = move_x 
        self.y = move_y

                # Go to next point
        if dirn[0] >= 0: # moving right
            if self.x >= x2:
                self.path_pos += 1
        else: # moving left
            if self.x <= x2:
                self.path_pos += 1

        if dirn[1] >= 0: # moving down
            if self.y >= y2:
                self.path_pos += 1
        else: # moving up
            if self.y <= y2:
                self.path_pos += 1



    def collide(self, x, y):
        # check if enemy is hit/range of tower
        if x < self.x + self.width and x > self.x:
            if y > self.y and y < self.y + self.height:
                return True
        return False

    def hit(self):
        # enemy hit

        pass