# Tank Class
# Class for general tank objects (player, enemeies)
from cmu_graphics import *
from Projectile import *
from Line import *
import math
import copy

class Tank:
    def __init__(self, x, y):
        # Objects that we take the alias of from app 
        self.grid = app.grid
        self.projectileManager = app.projectileManager
        self.objects = self.projectileManager.objects
        # Tank:
        self.degrees = 0
        self.width = 35
        self.height = 30

        self.x = x
        self.y = y
        self.r = 35
        self.borderWidth = 3

        # Change in angle while tank moves
        self.dAngle = 3

        # Default Color
        self.color = 'lightYellow'
        self.border = 'paleGoldenrod'
        
        # HitPoints of rectangle. 
        # Diagonal cutting user
        self.diag = ((self.width / 2) ** 2 + (self.height / 2) ** 2) ** 0.5
        # For the side hitpoints, we just need half of the width or height. 
        self.halfWid = self.width / 2
        self.halfHi = self.height / 2

        # Note that the first four are ordered in a rotation 
        # Top, Right, Bottom, Left
        self.hitAngles = [
            math.atan2(-self.height / 2, -self.width / 2), 
            math.atan2(-self.height / 2, self.width / 2), 
            math.atan2(self.height / 2, self.width / 2), 
            math.atan2(self.height / 2, -self.width / 2), 
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

        self.idxHighest = 0
        # Starting points (in order): Highest, Rightmost, Bottommost, Rightmost 
        self.idxHighestLeading = [0, 1, 2, 3]


        # Turret:
        self.turretDegrees = 0
        self.tubeColor = self.color
        self.tubeBorder = 'black'
        self.baseSize = 8
        self.capRad = 10

        # Tube - end of turret
        self.tubeLength = 30
        self.halfTube = 15
        # distance between the center of the tube and the tank. 
        self.tubeDistance = (self.baseSize + self.tubeLength) // 2
        self.tubeX = self.x - self.tubeDistance * math.cos(self.turretDegrees)
        self.tubeY = self.y - self.tubeDistance * math.sin(self.turretDegrees)
        self.tubeDegree = 0

        #Timer Constants
        self.stepCounts = 0
        self.timeInSecs = 0


    def __repr__(self):
        return 'Default Tank'


    def redraw(self, app):
        drawRect(self.x, self.y, self.width, self.height, border = self.border,
                borderWidth = self.borderWidth, fill = self.color, 
                align = 'center', rotateAngle = self.degrees)
        

        drawRect(self.tubeX, self.tubeY, self.tubeLength, self.baseSize,
                 align = 'center', rotateAngle = self.turretDegrees,
                 fill = self.tubeColor, border = self.tubeBorder)
        
        drawCircle(self.x, self.y, self.capRad, fill = self.tubeColor,
                   border = self.tubeBorder)
            
            
    def mouseMove(self, mouseX, mouseY):     
        pass
    
    def onStep(self, app):
        pass

    def mousePress(self, mouseX, mouseY):
        pass
            
    def keyPress(self, key):
        pass           
        
    def keyHold(self, keys):
        pass


    # Helper functions that check projectile and grid collisions as well as 
    # Aid with movement
     
    # Check to see if tank got hit by a projectile. 
    def checkHit(self, projectile):
        # Check highest point. 
        self.idxHighest = self.getHighestPoint()
        idxLowest = (self.idxHighest + 2) % 4
        
        # highest point, rightmost point, lowest Point, leftmost. 
        self.idxHighestLeading = [
            self.idxHighest,
            (self.idxHighest + 1) % 4,
            idxLowest,
            (self.idxHighest + 3) % 4,
        ]

        # Get the x coord of the leftmost and rightmost points. 
        right = self.hitPoints[self.idxHighestLeading[1]][0]
        left = self.hitPoints[self.idxHighestLeading[3]][0]

        # The topmost must be the lowest pos
        top = self.hitPoints[self.idxHighest][1] # Should have lower value
        bottom = self.hitPoints[idxLowest][1] # Should have higher value

        if ((top <= projectile.cY <= bottom)
             and (left <= projectile.cX <= right)):
            if self.degrees % 90 == 0:
                return False
            
            else:
                if self.checkLines(self.idxHighestLeading, projectile):
                    return False
                else:

                    return True
                
        else:
            return True
        

    # Check all the lines that comprise the rectangle and see if the projectile
    # Has passed through the tank. 
    def checkLines(self, cornerList, projectile):
        # Note that we start at the highest point
        for idx in range(len(cornerList)):
            # Create a line object that stretches between point 1 and 2
            point = self.hitPoints[idx]
            pointX = point[0]
            pointY = point[1]

            point2 = self.hitPoints[(idx + 1) % 4]
            point2X = point2[0]
            point2Y = point2[1]

            highestX = max(pointX, point2X)
            lowestX = min(pointX, point2X)

            # Remember that higher Y means lower point. 
            highestY = max(pointY, point2Y)
            lowestY = min(pointY, point2Y)

            if (projectile.cX, projectile.cY) in cornerList:
                return False

            # If is in-between the two points
            if ((lowestX <= projectile.cX <= highestX) 
                and (lowestY <= projectile.cY <= highestY)):
                connectingLine = Line(point, point2)
                
                # using point slope form of the line, determine if we're in or
                # out of the block 
                if connectingLine.evaluatePoint(idx, projectile):
                    return True

        return False
    

    # Return the point in the rectangle that has the lowest Y-value, 
    # Meaning that it's the highest point of the block. 
    def getHighestPoint(self):
        # Highest index - start 0 
        highest = 0
        # Gets the height of the hitpoint
        highestVal = self.hitPoints[0][1]

        for pointIdx in range(1, len(self.hitPoints)):
            # Lower value means higher position. 
            if self.hitPoints[pointIdx][1] < highestVal:
                highest = pointIdx
                highestVal = self.hitPoints[pointIdx][1]
            
            # Have the leftmost be the deciding factor for ties
            elif self.hitPoints[pointIdx][1] == highestVal:
                leaderLeftVal = self.hitPoints[highest][0]
                contenderLeftVal = self.hitPoints[pointIdx][0]
                
                # Lower value means more lef
                if leaderLeftVal > contenderLeftVal:
                    highest = pointIdx
                    highestVal = self.hitPoints[pointIdx][1]
        
        return highest

    # Check tanks' movement requests and update them if they are valid. 
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
    
    # Check a point to see if it's within bounds or not touching a cell. 
    def testNewPoints(self, testX, testY, testDegrees):
        testCopy = copy.deepcopy(self.hitPoints)
        self.updateHitPoints(testCopy, testX, testY, testDegrees)
        # Test bounds and cell collision - any could return false. 
        for hitX, hitY in testCopy:
            hitX = int(hitX)
            hitY = int(hitY)
            if ((not 0 <= hitX < self.grid.gWidth)
                 or (not 0 <= hitY < self.grid.gHeight)
                 or (not self.checkTankCollision(hitX, hitY))
                 or (not self.grid.checkPoint(hitX, hitY))):
                 return False
            
        return True
    
    # Check tank-to-tank collision
    def checkTankCollision(self, hitX, hitY):
        # Go through all tanks and check if it hits their radius
        for idx in range(len(app.objects)):
            # print(len(app.objects))
            print(idx, end = ' | ')
            print(app.objects[idx])
            tank = app.objects[idx]

            # print(self == tank)
            if (tank != self and 
                Tank.distance(hitX, hitY, tank.x, tank.y) <= self.r):
                    return False
        return True

    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                
    # Update all hitpoints based on what angle that are on relative to the tank 
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

