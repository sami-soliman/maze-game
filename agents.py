import pyglet
from pyglet.gl import *
import properties
from score import Score

class Player:
    def __init__(self,cellsize,off_setX,off_setYtop,off_setYbottom,rowsbycols,row,column):
        self.cellsize = cellsize
        self.off_setX = off_setX
        self.off_setYtop = off_setYtop
        self.off_setYbottom = off_setYbottom
        self.rowsbycols = rowsbycols
        self.cell_off_set = 10

        self.player_img = pyglet.image.load('images/player.png')
        self.player = self.player_img.get_texture()
        
        # columns for left to right
        # rows from bottom to top
        self.column = column
        self.row = row
        self.playerXcordinate = (self.off_setX+self.cell_off_set/2) + (self.cellsize*(self.column-1))
        self.playerYcordinate = (self.off_setYbottom+self.cell_off_set/2) + (self.cellsize*(self.row-1))

        # length for both width and height
        self.player_length = self.cellsize-self.cell_off_set

        # player moving direction will be updated in onkeypress function 
        self.player_direction = None

        # make game score
        self.score = Score(properties.score_initial_value)

    def draw(self):
        glEnable(GL_BLEND);
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        self.player.blit(self.playerXcordinate,self.playerYcordinate,0,width=self.player_length, height=self.player_length)

        # draw player score
        self.score.draw()

    def update_player_states(self,enemy_list,treasure,game):
        if self.player_direction == None:
            self.playerXcordinate = (self.off_setX+self.cell_off_set/2) + (self.cellsize*(self.column-1))
            self.playerYcordinate = (self.off_setYbottom+self.cell_off_set/2) + (self.cellsize*(self.row-1))
            self.score.update(self,enemy_list,treasure,game)

        if self.player_direction == 'right':
            if self.column < self.rowsbycols:
                self.column = self.column + 1
                self.playerXcordinate = (self.off_setX+self.cell_off_set/2) + (self.cellsize*(self.column-1))
                self.score.update(self,enemy_list,treasure,game)
        if self.player_direction == 'left':
            if self.column > 1:
                self.column = self.column -1
                self.playerXcordinate = (self.off_setX+self.cell_off_set/2) + (self.cellsize*(self.column-1))
                self.score.update(self,enemy_list,treasure,game)
        if self.player_direction == 'up':
            if self.row < self.rowsbycols:
                self.row = self.row +1
                self.playerYcordinate = (self.off_setYbottom+self.cell_off_set/2) + (self.cellsize*(self.row-1))
                self.score.update(self,enemy_list,treasure,game)
        if self.player_direction == 'down':
            if self.row > 1:
                self.row = self.row -1
                self.playerYcordinate = (self.off_setYbottom+self.cell_off_set/2) + (self.cellsize*(self.row-1))
                self.score.update(self,enemy_list,treasure,game)
        
    def update(self,enemy_list,treasure,game):
        self.update_player_states(enemy_list,treasure,game)



class Enemy:
    def __init__(self,cellsize,off_setX,off_setYtop,off_setYbottom,rowsbycols,row,column):
        self.cellsize = cellsize
        self.off_setX = off_setX
        self.off_setYtop = off_setYtop
        self.off_setYbottom = off_setYbottom
        self.rowsbycols = rowsbycols
        self.cell_off_set = 10

        self.enemy_img = pyglet.image.load('images/enemy.png')
        self.enemy = self.enemy_img.get_texture()
        
        # columns for left to right
        # rows from bottom to top
        self.column = column
        self.row = row
        self.enemyXcordinate = (self.off_setX+self.cell_off_set/2) + (self.cellsize*(self.column-1))
        self.enemyYcordinate = (self.off_setYbottom+self.cell_off_set/2) + (self.cellsize*(self.row-1))

        # length for both width and height
        self.enemy_length = self.cellsize-self.cell_off_set

    def draw(self):
        glEnable(GL_BLEND);
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        self.enemy.blit(self.enemyXcordinate,self.enemyYcordinate,0,width=self.enemy_length, height=self.enemy_length)


class Treasure:
    def __init__(self,cellsize,off_setX,off_setYtop,off_setYbottom,rowsbycols,row,column):
        self.cellsize = cellsize
        self.off_setX = off_setX
        self.off_setYtop = off_setYtop
        self.off_setYbottom = off_setYbottom
        self.rowsbycols = rowsbycols
        self.cell_off_set = 10

        self.treasure_img = pyglet.image.load('images/treasure.png')
        self.treasure = self.treasure_img.get_texture()
        
        # columns for left to right
        # rows from bottom to top
        self.column = column
        self.row = row
        self.treasureXcordinate = (self.off_setX+self.cell_off_set/2) + (self.cellsize*(self.column-1))
        self.treasureYcordinate = (self.off_setYbottom+self.cell_off_set/2) + (self.cellsize*(self.row-1))

        # length for both width and height
        self.treasure_length = self.cellsize-self.cell_off_set

    def draw(self):
        glEnable(GL_BLEND);
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        self.treasure.blit(self.treasureXcordinate,self.treasureYcordinate,0,width=self.treasure_length, height=self.treasure_length)
