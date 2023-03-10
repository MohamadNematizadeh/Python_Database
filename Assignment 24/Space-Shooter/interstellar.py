import random
import arcade
import time
import threading 
from class_spaceship import Spaceship
from enemy import Enemy
from threading import Thread
    
SCREEN_WIDTH = 600
SCREEN_HEHGHT = 600
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=800,title="Interstellar Geme_Mohammad 2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture("img/SaharaAndromeda_Coy_6135-scaled.jpeg")
        self.gameover_image = arcade.load_texture("img/GameOver.png")
        self.me = Spaceship(self.width)
        self.enemy_list = []
        self.game_start_time = time.time()
        self.my_thread = threading.Thread(target=self.new_enemy)
        self.my_thread.start()
        self.game_status = True
        self.start_time = time.time()
        self.speed = 2
        self.health_image = arcade.load_texture("img/ghalb2.png")

    def new_enemy(self):
            while True:
                self.speed+=0.5
                self.new_enemy = Enemy(self,self.enemy_list)
                self.doshman2.append(self.new_enemy)
                time.sleep(3)
  # برای نمایش
    def on_draw(self):
         arcade.start_render()
         arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
         self.me.draw()
         for enemy in self.enemy_list:
             enemy.draw()

         for bullet in self.me.bullet_list:
             bullet.draw()

         if self.game_status == False:

            arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEHGHT, self.gameover_image)    

    def on_key_press(self, symbol:int, modifiers:int):
        if symbol == arcade.key.LEFT:
            self.me.change_x = -1
        elif symbol == arcade.key.RIGHT:
            self.me.change_x = 1
        elif symbol == arcade.key.DOWN:
            self.me.change_x = 0    
        elif symbol == arcade.key.SPACE:
            self.me.fire()   
        elif symbol == 97: # left
            self.me.move("L")
        elif symbol == 100: #right
            self.me.move("R")    
    def on_key_release(self, symbol:int, modifiers:int):
        self.me.change_x = 0 


    def on_update(self, delta_time:float):
        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.me, enemy):
                arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEHGHT, self.gameover_image)
                exit(0)
               
        for enemy in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy , bullet):
                     self.enemy_list.remove(enemy)
                     self.me.bullet_list.remove(bullet)

        self.me.move()

        for enemy in self.enemy_list:
         enemy.move()
 
        for bullet in self.me.bullet_list:
             bullet.move() 
        for enemy in self.enemy_list:
            if enemy.center_y < 0:
                self.enemy_list.remove(enemy)

        if random.randint(1, 100) == 6:
         self.new_enemy = Enemy(self.width , self.height)
         self.enemy_list.append(self.new_enemy)


window = Game()
arcade.run()






