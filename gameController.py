import pyglet
import time
from grid import Grid
from agents import Player ,Enemy ,Treasure
from score import Score
import properties


class Game:
    def __init__(self):
        # creating the grid
        self.grid = Grid(5,properties.off_setX,properties.off_setYtop,
        properties.off_setYbottom,properties.grid_length,properties.cell_size)

        # creating the player 
        self.player = Player(properties.cell_size,properties.off_setX,properties.off_setYtop,
        properties.off_setYbottom,properties.rowsbycols,properties.player_initial_row,
        properties.player_initial_column)

        # adding 4 enemies
        self.enemy_list = []
        self.enemy_list.append( Enemy(properties.cell_size,properties.off_setX,properties.off_setYtop,
        properties.off_setYbottom,properties.rowsbycols,2,2) )
        self.enemy_list.append( Enemy(properties.cell_size,properties.off_setX,properties.off_setYtop,
        properties.off_setYbottom,properties.rowsbycols,4,2) )
        self.enemy_list.append( Enemy(properties.cell_size,properties.off_setX,properties.off_setYtop,
        properties.off_setYbottom,properties.rowsbycols,2,4) )
        self.enemy_list.append( Enemy(properties.cell_size,properties.off_setX,properties.off_setYtop,
        properties.off_setYbottom,properties.rowsbycols,4,4) )


        # adding treasure
        self.treasure = Treasure(properties.cell_size,properties.off_setX,properties.off_setYtop,
        properties.off_setYbottom,properties.rowsbycols,1,5)

        self.end = False
        self.number_of_trials = 3
    
    def game_start(self):
        pyglet.app.run()
    
    def game_restart(self):
        if self.number_of_trials == 0:
            self.game_over()
        
        self.player.row = properties.player_initial_row
        self.player.column = properties.player_initial_column
        self.player.score.score = properties.score_initial_value
        self.end = False
        self.number_of_trials -=1

    def game_over(self):
        pyglet.app.exit()
    
        
        