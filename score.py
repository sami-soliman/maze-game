import pyglet
import properties


class Score:
    def __init__(self,value):
        
        # player score
        self.scoreX = properties.off_setX
        self.scoreY = properties.off_setYbottom + properties.grid_length + 15
        self.score = value
        self.score_text = pyglet.text.Label('Score : ' + str(self.score),
        font_name='Times New Roman',font_size=20, color=(0,0,0,255),bold=True,
        x=self.scoreX, y=self.scoreY)


    def update(self,player,enemy_list,treasure,game):

        if player.player_direction != None:
            # for each step score decrease
            self.score -=1
            self.score_text.text = "Score :" + str(self.score)

            # check treasure
            if player.row == treasure.row and player.column == treasure.column:
                self.score += 100
                # update text
                self.score_text.text = "Score :" + str(self.score)
                game.end = True
                
            
            # check enemy
            for enemy in enemy_list:
                if player.row == enemy.row and player.column == enemy.column:
                    self.score -=100
                    # update text
                    self.score_text.text = "Score :" + str(self.score)
                    game.end = True
        else:
            self.score_text.text = "Score :" + str(self.score)

    def draw(self):
        self.score_text.draw()
