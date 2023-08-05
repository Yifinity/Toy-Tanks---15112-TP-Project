from cmu_graphics import *
from Projectile import *
import math
import copy

class Player:
    def __init__(self, app):
        # Objects that we take the alias of from app 
        self.grid = app.grid
        self.projectileManager = app.projectileManager

        # Tank:
        self.degrees = 0
        self.width = 35
        self.height = 30
        self.color = rgb(6, 6, 193)
        self.x = app.width / 2
        self.y = app.height / 2
        self.borderWidth = 3
        self.border = 'darkBlue'
        
        # HitPoints of rectangle. 
        # Diagonal cutting user
        self.diag = ((self.width / 2) ** 2 + (self.height / 2) ** 2) ** 0.5
        # For the side hitpoints, we just need half of the width or height. 
        self.halfWid = self.width / 2
        self.halfHi = self.height / 2

        self.hitAngles = [
            math.atan2(-self.height / 2, -self.width / 2), 
            math.atan2(-self.height / 2, self.width / 2), 
            math.atan2(self.height / 2, -self.width / 2), 
            math.atan2(self.height / 2, self.width / 2), 
            # Points that do not need the diagonal for points. 
            0,
            math.pi,
            math.pi / 2,
            -math.pi / 2
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
            (self.x + self.halfWid * math.cos(self.hitAngles[4] + self.degrees),
            self.y + self.halfWid * math.sin(self.hitAngles[4] + self.degrees)),
            (self.x + self.halfWid * math.cos(self.hitAngles[5] + self.degrees),
            self.y + self.halfWid * math.sin(self.hitAngles[5] + self.degrees)),
            (self.x + self.halfHi * math.cos(self.hitAngles[6] + self.degrees),
            self.y + self.halfHi * math.sin(self.hitAngles[6] + self.degrees)),
            (self.x + self.halfHi * math.cos(self.hitAngles[7] + self.degrees),
            self.y + self.halfHi * math.sin(self.hitAngles[7] + self.degrees))
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

        #Projectiles
        self.availableProjectiles = 5
        self.pY = 565
        self.pR = 10
        self.pX = app.width // 2 - (2 * 3 * self.pR)

        #Timer Constants
        self.stepCounts = 0
        self.timeInSecs = 0


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
        
        # Show how many projectiles we have 
        for projectIdx in range(self.availableProjectiles):
            pY, pX = self.pY, self.pX + (projectIdx * (3 * self.pR))
            drawCircle(pX, pY, self.pR, fill = 'black')
            
        for point in self.hitPoints:
            if point == 0 or point == 3:
                cX, cY = self.hitPoints[point]
                drawCircle(cX, cY, 5, fill = 'red')
            

    def mouseMove(self, mouseX, mouseY):     
        self.mX, self.mY = mouseX, mouseY
        self.followTarget()
    
    def onStep(self, app):
        # print(self.degrees)
        self.stepCounts += 1
        self.timeInSecs = self.stepCounts / 60
        
        # If we're out of projectiles - add one every half second. 
        if (self.availableProjectiles < 5 and self.timeInSecs % 0.5 == 0):
            self.availableProjectiles += 1

    
    def mousePress(self, mouseX, mouseY):
        # Ensure that we're not violating any timer rules. 
        # Calculate the x and y vals using trigonometry. 
        if self.availableProjectiles > 0:
            trigX =  15 * math.cos(math.radians(self.turretDegrees))
            trigY = 15 * math.sin(math.radians(self.turretDegrees))
            projectileX = self.tubeX - trigX
            projectileY = self.tubeY - trigY
            
            self.projectileManager.projectiles.append(
                Projectile(projectileX, projectileY, 
                            math.radians(self.turretDegrees), self.grid))
    
            self.availableProjectiles -= 1
            self.stepCounts = 0  
            
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
        self.checkBounds(newX, newY, newDegrees)

        # No matter what direction we go, update the turret to follow
        self.followTarget()
    
    def checkHit(self, projectile):
        if self.degrees % 90 == 0:
            top, left = self.hitPoints[0][0], self.hitPoints[0][1]
            bottom, right = self.hitPoints[3][0], self.hitPoints[3][1]

            if ((left <= projectile.cX <= right)
                and (bottom <= projectile.cY <= top)):
                return False
            else:
                return True
        else:
            return True



    def checkBounds(self, newX, newY, newDegrees):
        xQualifies = True
        yQualifies = True
        degQualifies = True
        
        # Degrees are the most important - so check that first. 
        degQualifies = self.testNewPoints(self.x, self.y, newDegrees)
        if degQualifies:
            # Update the degrees if it passes, so we can now pass that on
            self.degrees = newDegrees
        
        xQualifies = self.testNewPoints(newX, self.y, self.degrees)
        if xQualifies:
            self.x = newX
        
        yQualifies = self.testNewPoints(self.x, newY, self.degrees)
        if yQualifies:
            self.y = newY

        # Update new hitPoints
        self.updateHitPoints(self.hitPoints, self.x, self.y, self.degrees)
    
    def testNewPoints(self, testX, testY, testDegrees):
        testCopy = copy.deepcopy(self.hitPoints)

        self.updateHitPoints(testCopy, testX, testY, testDegrees)
        # Test bounds and cell collision - any could return false. 
        for hitX, hitY in testCopy:
            hitX = int(hitX)
            hitY = int(hitY)
            if ((not 0 <= hitX < self.grid.gWidth)
                 or (not 0 <= hitY < self.grid.gHeight)
                 or (not self.grid.checkPoint(hitX, hitY))):
                 return False
            
        return True


    # Goes through all hitpoints, and modifies points as nessisary. 
    def updateHitPoints(self, pointsList, modX, modY, degrees):
        inputRads = math.radians(degrees)
        for rads in range(len(self.hitAngles)):
            newRads = self.hitAngles[rads] + inputRads
            
            # The last two should have length of the width / 2
            if rads < 4:
                # For the front and back points, we just want half of the width
                currentX = modX + self.diag * math.cos(newRads)
                currentY = modY + self.diag * math.sin(newRads)        

            elif rads < 6:
                currentX = modX + self.halfWid * math.cos(newRads)
                currentY = modY + self.halfWid * math.sin(newRads)  

            else:
                currentX = modX + self.halfHi * math.cos(newRads)
                currentY = modY + self.halfHi * math.sin(newRads)  

            pointsList[rads] = (currentX, currentY)


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