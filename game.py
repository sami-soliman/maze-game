import pyglet
from pyglet.gl import *
from pyglet.window import key
from grid import Grid
from agents import Player ,Enemy ,Treasure
from score import Score
from gameController import Game
import properties

class MyWindow(pyglet.window.Window):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        # background color red green blue alpha
        glClearColor(1,1,1,0)

        # making game controller
        self.game = Game()


    def on_key_press(self,symbol,modifiers):
        if self.game.end == False:
            if symbol == key.RIGHT:
                self.game.player.player_direction = 'right'
                self.update()
            if symbol == key.LEFT:
                self.game.player.player_direction = 'left'
                self.update()
            if symbol == key.UP:
                self.game.player.player_direction = 'up'
                self.update()
            if symbol == key.DOWN:
                self.game.player.player_direction = 'down'
                self.update()
    
    def on_key_release(self,symbol,modifiers):
        self.game.player.player_direction = None
        if self.game.end == True:
            self.game.game_restart()
            self.update()


    def on_draw(self):
        self.clear()
        self.game.grid.draw()
        self.game.player.draw()
        for enemy in self.game.enemy_list:
            enemy.draw()
        self.game.treasure.draw()


    def update(self): 
        self.game.player.update(self.game.enemy_list,self.game.treasure,self.game)
        
        

if __name__=="__main__":
    window = MyWindow(properties.window_width,properties.window_height,"maze",resizable = False)
    window.set_location( 300, 50)
    #pyglet.clock.schedule_interval(window.update,properties.frame_rate)
 
    window.game.game_start()
