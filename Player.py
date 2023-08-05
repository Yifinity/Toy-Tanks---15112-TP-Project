from cmu_graphics import *
from Projectile import *
from Grid import *
import math

class Player:
    def __init__(self, grid):
        # Send the grid in to ensure we follow the bounds. 
        self.grid = grid

        # Tank:
        self.degrees = 0
        self.width = 35
        self.height = 30
        self.color = rgb(6, 6, 193)
        self.x = app.width / 2
        self.y = app.height / 2
        self.borderWidth = 3
        self.border = 'darkBlue'
        
        # Points on hitPoints of rectangle. 
        # Diagonal cutting user
        self.diag = ((self.width / 2) ** 2 + (self.height / 2) ** 2) ** 0.5

        self.hitAngles = [
            math.atan2(-self.height / 2, -self.width / 2), 
            math.atan2(-self.height / 2, self.width / 2), 
            math.atan2(self.height / 2, -self.width / 2), 
            math.atan2(self.height / 2, self.width / 2), 
            # Add two points at the beginning and end of the rectangle. 
            0,
            math.pi,
            ]

        self.hitPoints = [
            (self.x + self.diag * math.cos(self.hitAngles[0] + self.degrees),
            self.y + self.diag * math.sin(self.hitAngles[0] + self.degrees)),
            (self.x + self.diag * math.cos(self.hitAngles[1] + self.degrees),
            self.y + self.diag * math.sin(self.hitAngles[1] + self.degrees)),
            (self.x + self.diag * math.cos(self.hitAngles[2] + self.degrees),
            self.y + self.diag * math.sin(self.hitAngles[2] + self.degrees)),
            (self.x + self.diag * math.cos(self.hitAngles[3] + self.degrees),
            self.y + self.diag * math.sin(self.hitAngles[3] + self.degrees)),
            (self.x + self.diag * math.cos(self.hitAngles[4] + self.degrees),
            self.y + self.diag * math.sin(self.hitAngles[4] + self.degrees)),
            (self.x + self.diag * math.cos(self.hitAngles[5] + self.degrees),
            self.y + self.diag * math.sin(self.hitAngles[5] + self.degrees)),
        ]
        
        #Mouse:
        self.mX = app.width // 2
        self.mY = app.height // 2
        self.mCol = None
        self.mVis = False # is circle visible. 
        self.mRad = 50
        self.mBorderWidth = 10

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
        self.dAngle = 3

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
        
        drawCircle(self.mX, self.mY, self.mRad, fill = self.mCol,
                   visible = self.mVis, border = self.color, 
                  borderWidth = self.mBorderWidth)
        
        for (corX, corY) in self.hitPoints:
            drawCircle(corX, corY, 2, fill = None, border = 'red', 
                   borderWidth = 1)
            
        for projectile in self.projectiles:
            projectile.drawProjectile(app)
        
    def mouseMove(self, mouseX, mouseY):     
        self.mX, self.mY = mouseX, mouseY
        self.followTarget()
    
    def onStep(self, app):
        pass

    def mousePress(self, mouseX, mouseY):
        # Limit shots to five at a time. 
        if len(self.projectiles) < 5: 
            # Calculate the dX and dY using trigonometry. 
            trigX =  15 * math.cos(math.radians(self.turretDegrees))
            trigY = 15 * math.sin(math.radians(self.turretDegrees))
            projectileX = self.tubeX - trigX
            projectileY = self.tubeY - trigY
                        
            self.projectiles.append(
                Projectile(projectileX, projectileY, 
                           math.radians(self.turretDegrees), self.grid))

    def keyPress(self, key):
        pass           
        
    def keyHold(self, keys):
        newX, newY, newDegrees = self.x, self.y, self.degrees
        # if-elif pairs ensures no control conflicts
        if 'w' in keys:
            newX += 2 * math.cos(math.radians(self.degrees))
            newY += 2 * math.sin(math.radians(self.degrees))
            
        elif 's' in keys: 
            newX -= 2 * math.cos(math.radians(self.degrees))
            newY -= 2 * math.sin(math.radians(self.degrees))

        if 'a' in keys: 
            newDegrees -= self.dAngle

        elif 'd' in keys:
            newDegrees += self.dAngle      
        
        # Make sure that the new bounds work - if so, we'll implement them. 
        self.checkBounds(app, newX, newY, newDegrees)

        # No matter what direction we go, update the turret to follow
        self.followTarget()
    
    def checkBounds(self, app, newX, newY, newDegrees):
        xQualifies = True
        yQualifies = True
        degQualifies = True
        
        # Verify that these new move requests work and go to default if not
        # Update our points in our hitPoints. 
        for rads in range(len(self.hitAngles)):
            newRads = math.radians(newDegrees)
            cornerX = int(newX + self.diag * math.cos(self.hitAngles[rads] + newRads))
            cornerY = int(newY + self.diag * math.sin(self.hitAngles[rads] + newRads))

            if ((not xQualifies) or (not 0 <= cornerX < self.grid.gWidth)
                 or (not self.grid.checkPoint(cornerX, cornerY))):
                    xQualifies = False
            
            if ((not yQualifies) or (not 0 <= cornerY < self.grid.gHeight)
                 or (not self.grid.checkPoint(cornerX, cornerY))):
                    yQualifies = False

        # Ensure we're in the grid
        if (xQualifies): 
            self.x = newX

        if (yQualifies):
            self.y = newY
        
        # Update new hitPoints
        self.updateHitPoints(newDegrees)
        self.degrees = newDegrees
 

    # Goes through all hitpoints, and modifies points as nessisary. 
    def updateHitPoints(self, degrees):
        inputRads = math.radians(degrees)
        for rads in range(len(self.hitAngles)):
            newRads = self.hitAngles[rads] + inputRads
            
            # The last two should have length of the width / 2
            if rads == 4 or rads == 5:
                # For the front and back points, we just want half of the width
                halfWidth = self.width / 2
                currentX = self.x + halfWidth * math.cos(newRads)
                currentY = self.y + halfWidth * math.sin(newRads)  

            else:
                currentX = self.x + self.diag * math.cos(newRads)
                currentY = self.y + self.diag * math.sin(newRads)        

            self.hitPoints[rads] = (currentX, currentY)


    # *Helper have the turret follow the mouse position. 
    def followTarget(self):
        self.differenceX = self.x - self.mX
        self.differenceY = self.y - self.mY 

        # have no circle appear if we're too close
        if (self.differenceX ** 2 + self.differenceY ** 2) ** 0.5 < self.mRad:
            self.mVis = False

        else:
            self.mVis = True

        # Get our degrees using inverse tan
        self.turretDegrees = math.degrees(
                                math.atan2(self.differenceY, self.differenceX))
        # Degrees needed for trigonometry
        trigDegrees = math.radians(self.turretDegrees)
        self.tubeX = self.x - self.tubeDistance * math.cos(trigDegrees)
        self.tubeY = self.y - self.tubeDistance * math.sin(trigDegrees)