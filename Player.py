from cmu_graphics import *
import math

class Player:
    def __init__(self):
        # Tank:
        self.degrees = 0
        self.width = 35
        self.height = 30
        self.color = rgb(6, 6, 193)
        self.x = app.width / 2
        self.y = app.height / 2
        self.border = 'darkBlue'
        self.borderWidth = 3

        #Mouse:
        self.mX = 0
        self.mY = 0

        # Turret:
        self.turretDegrees = 0
        self.tubeColor = rgb(75, 75, 255)
        self.tubeBorder = 'black'
        self.baseSize = 8
        self.capRad = 10

        # Tube - end of turret
        self.tubeLength = 30
        self.tubeX = self.x - self.baseSize / 2
        self.tubeY = self.y - self.baseSize / 2
        self.tubeDegree = 0

        # Change in angle
        self.dAngle = 5

    
    def redraw(self, app):
        drawRect(self.x, self.y, self.width, self.height, border = self.border,
                borderWidth = self.borderWidth, fill = self.color, 
                align = 'center', rotateAngle = self.degrees)
        
        drawRect(self.tubeX, self.tubeY, self.tubeLength, self.baseSize,
                 align = 'center', rotateAngle = self.turretDegrees,
                 fill = self.tubeColor, border = self.tubeBorder)
        
        drawCircle(self.x, self.y, self.capRad, fill = self.tubeColor,
                   border = self.tubeBorder)
        
        drawCircle(self.mX, self.mY, 50, fill = None, border = self.color, 
                   borderWidth = 10)
        
    def mouseMove(self, mouseX, mouseY):     
        self.mX, self.mY = mouseX, mouseY
        self.followTarget()
    
    # Have the turret follow the mouse position. 
    def followTarget(self):
        differenceX = self.x - self.mX
        differenceY = self.y - self.mY 
        # Get our degrees using inverse tan
        self.turretDegrees = math.degrees(math.atan2(differenceY, differenceX))

        # Degrees needed for trigonometry
        trigDegrees = math.radians(self.turretDegrees)

        # distance between the center of the tube and the tank. 
        tubeDistance = (self.baseSize + self.tubeLength) // 2
        self.tubeX = self.x - tubeDistance * math.cos(trigDegrees)
        self.tubeY = self.y - tubeDistance * math.sin(trigDegrees)

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
        
        # No matter what direction we go, update the turret to follow
        self.followTarget()



