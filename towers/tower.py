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
        self.damage = 1

    def draw(self, win):
        img = self.tower_imgs[self.lvl]
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))

    def draw_range(self, win):
        if self.selected:
            surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (50, 50, 50, 64), (self.range, self.range), self.range, 0)
            win.blit(surface, (self.x - self.range, self.y - self.range))


    def click(self, x, y):
        # Returns bool for if tower is clicked
        img = self.tower_imgs[self.lvl]
        width = img.get_width()
        height = img.get_height()
        if (self.x - width // 2) <= x <= (self.x + width // 2) and (self.y - height // 2) <= y <= (self.y + height // 2):
            return True
        return False


    def sell(self):
        #sell tower, return sell price
        return self.sell_price[self.lvl - 1]
        pass

    def upgrade(self):
        #upgrade tower
        self.lvl += 1
        self.damage += 1

    def get_upgrade_cost(self):
        #return upgrade cost
        return self.price[self.lvl - 1]

    def move(self, x, y):
        self.x = x
        self.y = y