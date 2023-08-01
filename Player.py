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
        self.turretColor = 'lightBlue'
        self.tubeColor = 'brown'
        self.baseSize = 10
        self.tubeLength = 20
        self.tubeX = self.x - self.baseSize / 2
        self.tubeY = self.y + self.baseSize / 2

        # This is the hypotenuse of a 45-45-90 triangle - the turret
        self.turretDiag = 5 * math.sqrt(2)
        self.tubeDegree = 0

        # Change in angle
        self.dAngle = 5

        # self.lPointX = 0
        # self.lPointY = 0
        
        self.rPointX = 0
        self.rPointY = 0
    
    def redraw(self, app):
        drawRect(self.x, self.y, self.width, self.height,
                fill = self.color, align = 'center', rotateAngle = self.degrees)
        
        drawRect(self.x, self.y, self.baseSize, self.baseSize, align = 'center',
                fill = self.turretColor, rotateAngle = self.turretDegrees)
    
        # Draw Angled Rect:

        # drawRect(self.tubeX, self.tubeY, self.tubeLength, self.baseSize,
        #         fill = self.tubeColor)

        drawCircle(self.mX, self.mY, 50, fill = None, border = self.color, 
                   borderWidth = 10)
        
        # drawCircle(self.lPointX, self.lPointY, 10, fill = None, border = "yellow", 
                #    borderWidth = 1)
        
        drawCircle(self.rPointX, self.rPointY, 10, fill = None, border = "red", 
                   borderWidth = 1)
        
    def mouseMove(self, mouseX, mouseY):
        differenceX = self.x - mouseX
        differenceY = self.y - mouseY
        self.turretDegrees = math.degrees(math.atan2(differenceY, differenceX))

        self.drawAngleRect((self.x, self.y), ((self.x + self.turretDiag), self.y), self.turretDegrees)
        
        # rotate(origin, point, angle)        
        self.mX, self.mY = mouseX, mouseY

    
    def drawAngleRect(self, origin, centerPoint, rotationDegree):
        # leftBase = Player.rotate(origin, centerPoint, -rotationDegree // 2)
        rightBase = Player.rotate(origin, centerPoint, rotationDegree // 2)
        # self.lPointX, self.lPointY = leftBase
        self.rPointX, self.rPointY = rightBase

    # A good explination on how to rotate a point about a point
    # Direct copy and paste. 
    # https://stackoverflow.com/questions/34372480/rotate-point-about-another-point-in-degrees-python
    @staticmethod
    def rotate(origin, point, angle):
        ox, oy = origin
        px, py = point

        angle = math.radians(angle) # Convert radians needed for trigonometry
        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)        
        
        return qx, qy

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

