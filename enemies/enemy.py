import pygame
import math

class Enemy:
    img = []

    def __init__(self):
        self.width = 64
        self.height = 64
        self.health = 1
        self.img = None
        self.path = [(-70, 436), (15, 436), (191, 435), (191, 205), (436, 205), (444, 509), (753, 514), (756, 363), (1178, 356), (1190, 357), (1400, 357), (1470, 357)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.path_pos = 0
        self.vel = 3
        self.move_count = 0
        self.move_dis = 0
        self.dis = 0
        self.max_health = 1

    def draw(self, win):
        # draw enemy
        if self.img:
            win.blit(self.img, (self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2))
        self.draw_health_bar(win)
        self.move()

    def move(self):
        if self.path_pos < len(self.path) - 1:
            x1, y1 = self.path[self.path_pos]
            x2, y2 = self.path[self.path_pos + 1]

            # Calculate direction vector and normalize it
            dirn = (x2 - x1, y2 - y1)
            length = math.sqrt(dirn[0] ** 2 + dirn[1] ** 2)
            dirn = (dirn[0] / length, dirn[1] / length)

            # Move enemy by velocity in the direction
            self.x += dirn[0] * self.vel
            self.y += dirn[1] * self.vel

            # Check if the enemy has reached (or passed) the next point
            if (dirn[0] >= 0 and self.x >= x2) or (dirn[0] < 0 and self.x <= x2):
                if (dirn[1] >= 0 and self.y >= y2) or (dirn[1] < 0 and self.y <= y2):
                    self.path_pos += 1
                    self.x, self.y = self.path[self.path_pos]  # Correct position to the exact path point

    def draw_health_bar(self, win):
        length = 50
        move_By = round(length / self.max_health)
        health_bar = move_By * self.health

        pygame.draw.rect(win, (255,0,0), (self.x - 25, self.y - 40, length, 10), 0)
        pygame.draw.rect(win, (0,255,0), (self.x - 25, self.y - 40, health_bar, 10), 0)

    def collide(self, x, y):
        # check if enemy is hit/range of tower
        if x <= self.x + self.width and x >= self.x:
            if y <= self.y + self.height and y >= self.y:
                return True
        return False

    def hit(self):
        # enemy hit

        self.health -= 1
        if self.health <= 0:
            return True
        return False
