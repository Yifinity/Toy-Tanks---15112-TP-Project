from cmu_graphics import *
import math

class Player:
    def __init__(self):
        # Tank:
        self.degrees = 0
        self.width = 40
        self.height = 35
        self.color = 'darkBlue'
        self.x = app.width / 2
        self.y = app.height / 2

        #Mouse:
        self.mX = 0
        self.mY = 0

        # Turret:
        self.turretDegrees = 0
        self.tubeColor = 'lightBlue'
        self.tubeBorder = 'black'
        self.baseSize = 10

        # Tube - end of turret
        self.tubeLength = 30
        self.tubeX = self.x - self.baseSize / 2
        self.tubeY = self.y - self.baseSize / 2

        self.tubeDegree = 0

        # Change in angle
        self.dAngle = 5

    
    def redraw(self, app):
        drawRect(self.x, self.y, self.width, self.height,
                fill = self.color, align = 'center', rotateAngle = self.degrees)
        
        # drawRect(self.x, self.y, self.baseSize, self.baseSize, align = 'center',
        #         fill = self.turretColor, rotateAngle = self.turretDegrees)
    
        drawRect(self.tubeX, self.tubeY, self.tubeLength, self.baseSize,
                 align = 'center', rotateAngle = self.turretDegrees,
                 fill = self.tubeColor, border = self.tubeBorder)

        drawCircle(self.x, self.y, 15, fill = self.tubeColor, border = self.tubeBorder)

        drawCircle(self.mX, self.mY, 50, fill = None, border = self.color, 
                   borderWidth = 10)
        
    def mouseMove(self, mouseX, mouseY):
        # rotate(origin, point, angle)        
        self.mX, self.mY = mouseX, mouseY
        self.followTarget()
    
    def followTarget(self):
        differenceX = self.x - self.mX
        differenceY = self.y - self.mY 

        self.turretDegrees = math.degrees(math.atan2(differenceY, differenceX))
        
        tubeBaseDistance = (self.baseSize + self.tubeLength) // 2
        self.tubeX = self.x - tubeBaseDistance * math.cos(math.radians(self.turretDegrees))
        self.tubeY = self.y - tubeBaseDistance * math.sin(math.radians(self.turretDegrees))

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
        
        self.followTarget()



