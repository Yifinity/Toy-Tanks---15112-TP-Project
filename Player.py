from cmu_graphics import *
from Projectile import *
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
        self.mX = app.width // 2
        self.mY = app.height // 2

        # Turret:
        self.differenceX = self.x - self.mX
        self.differenceY = self.y - self.mY 
        self.turretDegrees = math.degrees(
                                math.atan2(self.differenceY, self.differenceX))
        self.tubeColor = rgb(75, 75, 255)
        self.tubeBorder = 'black'
        self.baseSize = 8
        self.capRad = 10

        # Tube - end of turret
        self.tubeLength = 30
        # distance between the center of the tube and the tank. 
        self.tubeDistance = (self.baseSize + self.tubeLength) // 2
        self.tubeX = self.x - self.tubeDistance * math.cos(self.turretDegrees)
        self.tubeY = self.y - self.tubeDistance * math.sin(self.turretDegrees)
        self.tubeDegree = 0

        # Change in angle
        self.dAngle = 2

        # Track projectiles
        self.projectiles = []

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
        
        for projectile in self.projectiles:
            projectile.drawProjectile(app)
        
    def mouseMove(self, mouseX, mouseY):     
        self.mX, self.mY = mouseX, mouseY
        self.followTarget()
    
    def onStep(self, app):
        pass

    def mousePress(self, mouseX, mouseY):
        # Limit shots to five at a time. 
        if len(self.projectiles) <= 5: 
            projectileX = self.tubeX - 15 * math.cos(math.radians(self.turretDegrees))
            projectileY = self.tubeY - 15 * math.sin(math.radians(self.turretDegrees))
                        
            self.projectiles.append(
                Projectile(projectileX, projectileY, 
                           math.radians(self.turretDegrees)))

    def keyPress(self, key):
        pass           
        
    def keyHold(self, keys):
        newX, newY, newDegrees = self.x, self.y, self.degrees
        # if-elif pairs ensures no control conflict
        if 'w' in keys:
            newX += 2 * math.cos(math.radians(self.degrees))
            newY +=  2 * math.sin(math.radians(self.degrees))
            
        elif 's' in keys: 
            newX -= 2 * math.cos(math.radians(self.degrees))
            newY -= 2 * math.sin(math.radians(self.degrees))

        if 'a' in keys: 
            newDegrees -= self.dAngle

        elif 'd' in keys:
            newDegrees += self.dAngle      
        
        self.checkBounds(app, newX, newY, newDegrees)
        # No matter what direction we go, update the turret to follow
        self.followTarget()
    
    def checkBounds(self, app, newX, newY, newDegrees):
        # Verify that these new move requests work and go to default if no
        if (0 <= newX < app.width):
            self.x = newX

        if (0 <= newY < app.height):
            self.y = newY
        
        self.degrees = newDegrees



    # *Helper have the turret follow the mouse position. 
    def followTarget(self):
        self.differenceX = self.x - self.mX
        self.differenceY = self.y - self.mY 
        # Get our degrees using inverse tan
        self.turretDegrees = math.degrees(
                                math.atan2(self.differenceY, self.differenceX))
        # Degrees needed for trigonometry
        trigDegrees = math.radians(self.turretDegrees)
        self.tubeX = self.x - self.tubeDistance * math.cos(trigDegrees)
        self.tubeY = self.y - self.tubeDistance * math.sin(trigDegrees)