from cmu_graphics import *

class Player:
    def __init__(self):
        self.width = 40
        self.height = 30
        self.color = 'darkBlue'
        self.x = app.width / 2
        self.y = app.height / 2
        self.dPos = 3
        self.dAngle = 2
    
        self.angle = 0

    def redraw(self, app):
        drawRect(self.x, self.y, self.width, self.height,
                fill = self.color, align = 'center', rotateAngle = self.angle)
        
    def keyPress(self, key):
        pass           
        
    def keyHold(self, keys):
        # if-elif pairs ensures no control conflict
        if 'w' in keys:
            self.x += self.dPos
        elif 's' in keys: 
            self.x -= self.dPos
        
        if 'a' in keys: 
            self.angle += self.dAngle
        elif 'd' in keys:
            self.angle -= self.dAngle          

