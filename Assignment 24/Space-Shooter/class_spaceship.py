import arcade
from bollet import Bullet
class Spaceship(arcade.Sprite):
    def __init__ (self, w):
        super().__init__("img/12.png")
        self.center_x = w//2
        self.center_y = 57
        self.change_x = 0
        self.change_y = 0
        self.width  = 99
        self.height = 99
        self.speed = 4
        self.game_width = w
        self.bullet_list = []
        self.health = 3



    def move(self):
        if self.change_x == -1:
            if self.center_x > 0:
                self.center_x -=self.speed

        elif self.change_x == 1 :
            if self.center_x < self.game_width:
                self.center_x +=self.speed 

    def fire(self):
        new_bullet = Bullet(self)
        self.bullet_list.append(new_bullet)
                  