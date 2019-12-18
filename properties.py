window_length = 600
frame_rate = 30/60.0


#####  Grid ##########
rowsbycols = 5

off_setX = 10
off_setYtop = 50
off_setYbottom = 10

window_width = window_length + (2*off_setX)
window_height = window_length + off_setYtop + off_setYbottom

grid_length = window_length
cell_size = int( grid_length / rowsbycols)

####################
player_initial_row = 5
player_initial_column = 1

score_initial_value = 0