import random
import arcade
class Enemy(arcade.Sprite):
    def __init__(self,w,h,s=3):
        super().__init__("img/bullet2.png")
        self.center_x = random.randint(0,w)
        self.center_y = h+24
        self.angle = 180
        self.width  = 48
        self.height = 48
        self.speed = s

    def move(self):
         self.center_y-= self.speed