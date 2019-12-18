## useless file just some code i can use 
class Line:
    def __init__(self ,fposx,fposy,sposx,sposy):
        self.fposx = fposx
        self.fposy = fposy
        self.sposx = sposx
        self.sposy = sposy

        self.vertices = pyglet.graphics.vertex_list( 2,('v2i/stream',[self.fposx,self.fposy ,self.sposx,self.sposy])
                                                      ,('c3B',[255,0,0 ,255,0,0]) )
                                                      

    def draw(self):
        self.vertices.draw(pyglet.gl.GL_LINES)
        print('line ondraw called')

    def update(self,dt):
        self.fposx += int(100*dt)
        self.vertices = pyglet.graphics.vertex_list( 2,('v2i',[self.fposx,self.fposy ,self.sposx,self.sposy])
                                                      ,('c3B',[255,0,0 ,255,0,0]) )
        print('line update called' + str(self.fposx))
    
#############################


self.line = Line(400,400,600,400)
        #self.line = Line(0,0,0.5,0.5)

        #self.img = pyglet.image.load('PlayerShip.png')
        #self.texture = self.img.get_texture()

##################################

self.line.draw()      
glEnable(self.texture.target)
glBindTexture(self.texture.target, self.texture.id)
self.texture.target= GL_TEXTURE_2D
self.texture.blit(0,0.5,0,width=50, height=50)
glDisable(self.texture.target)

###############################
        self.line.update(dt)
###############################
'''
    def on_resize(self,width,height):
        #glViewport(0,0,width,height)
        print('resized')
    '''
