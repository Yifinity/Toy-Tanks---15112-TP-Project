from cmu_graphics import *
import math

class Player:
    def __init__(self):
        self.width = 40
        self.height = 35
        self.color = 'darkBlue'
        self.turretColor = 'blue'
        self.x = app.width / 2
        self.y = app.height / 2

        #Mouse:
        self.mX = 0
        self.mY = 0


        self.degrees = 0
        self.turretDegrees = 0

        # Change in angle
        self.dAngle = 5

    
    def redraw(self, app):
        drawRect(self.x, self.y, self.width, self.height,
                fill = self.color, align = 'center', rotateAngle = self.degrees)
        
        drawRect(self.x, self.y, 30, 10, fill = self.turretColor,
                align = 'center', border = "black", 
                rotateAngle = self.turretDegrees)
    
        drawCircle(self.mX, self.mY, 50, fill = None, border = self.color, 
                   borderWidth = 10)
    
    def mouseMove(self, mouseX, mouseY):
        differenceX = self.x - mouseX
        differenceY = self.y - mouseY
        self.turretDegrees = math.degrees(math.atan2(differenceY, differenceX))

        self.mX, self.mY = mouseX, mouseY

    def keyPress(self, key):
        pass           
        
    def keyHold(self, keys):
        # if-elif pairs ensures no control conflict
        if 'w' in keys:
            self.x += 4 * math.cos(math.radians(self.degrees))
            self.y +=  4 * math.sin(math.radians(self.degrees))
            
        elif 's' in keys: 
            self.x -= 4 * math.cos(math.radians(self.degrees))
            self.y -= 4 * math.sin(math.radians(self.degrees))

        if 'a' in keys: 
            self.degrees -= self.dAngle
        elif 'd' in keys:
            self.degrees += self.dAngle          

