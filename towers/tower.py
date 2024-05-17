import pygame



#ABSTARCT CLASS
class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0,0,0]
        self.price = [0,0,0]
        self.lvl = 0
        self.selected = False
        self.menu = None
        self.tower_imgs = []

    def draw(self, win):
        img = self.tower_imgs[self.lvl]
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))

    def click(self, x, y):
        #returns bool for if tower is clicked
        if x <= self.x + self.width and x >= self.x:
            if y <= self.y + self.height and y >= self.y:
                return True
        return False

    def sell(self):
        #sell tower, return sell price
        return self.sell_price[self.lvl - 1]
        pass

    def upgrade(self):
        #upgrade tower
        self.lvl += 1

    def get_upgrade_cost(self):
        #return upgrade cost
        return self.price[self.lvl - 1]

    def move(self):
        self.x = x
        self.y = y