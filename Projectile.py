from cmu_graphics import *
from Grid import *
import math
# from Player import *

class Projectile:
    def __init__(self, cX, cY, cAngle):
        # get our grid to verify bounds. 
        self.grid = app.grid

        self.cX = cX
        self.cY = cY
        self.cAngle = cAngle # Face in right direction
        self.cRadius = 4 # tank's barrel is 8 pxls

        # Change in dX and dY
        # Zero points to left, so flip sign of dX and dY
        self.dX = -1.15 * (math.cos(self.cAngle))
        self.dY = -1.15 * (math.sin(self.cAngle))


        self.bounceAmount = 0

    def drawProjectile(self, app):
        # Create our projectile
        drawCircle(self.cX, self.cY, self.cRadius, fill = 'grey')
    
    def onStep(self):
        # Handle bounces
        self.cX += self.dX
        self.cY += self.dY

 
    def checkCollision(self, app):
        # Look three points ahead
        newX = self.cX + self.dX
        newY = self.cY + self.dY

        if ((0 <= newX < self.grid.gWidth) and (0 <= newY < self.grid.gHeight)
             and self.grid.checkPoint(newX, newY)):
            return True
        
        else: # New position doesn't work.             
            if self.bounceAmount < 1: 
                # First check if we're out of bounds
                if (not 0 <= self.cX < self.grid.gWidth): 
                    self.dX *= -1

                elif (not 0 <= self.cY < self.grid.gHeight):
                    self.dY *= -1
                
                # Check and manage grid collisions
                else: 
                    self.manageGridCollision(newX, newY)
                
                # update bounce count
                self.bounceAmount += 1                 
                return True
            
            else:
                # If both cases fail, 
                return False
    
    # Use a recursive function to find whether we had an x or y bounce
    def manageGridCollision(self, testX, testY):
        # Amount of times we need to get out of a grid 
        xCounter = self.countRevertTimes(0, testX, testY,  True)
        yCounter = self.countRevertTimes(0, testX, testY, False)
        print(xCounter, yCounter)

        if xCounter > yCounter:
            # If removing the y led one to get out of the grid faster, 
            self.dY *= -1
        
        elif xCounter < yCounter:
            self.dX *= -1
        
        else:
            # if both had equal count amounts, do both
            self.dX *= -1
            self.dY *= -1


    def countRevertTimes(self, count, testX, testY, testXValue):
        # set a limit to our count
        if self.grid.checkPoint(testX, testY) or count > 10:
            return count
        
        else:
            # If we're testing the x value, 
            if testXValue:
                testX -= self.dX # revert x value
                return self.countRevertTimes(count + 1, testX, testY, True)
            
            else:
                testY -= self.dY
                return self.countRevertTimes(count + 1, testX, testY, False)


