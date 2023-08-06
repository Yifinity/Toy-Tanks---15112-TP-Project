from cmu_graphics import *
from Grid import *
import math
# from Player import *

class Projectile:
    def __init__(self, app, cX, cY, cAngle):
        # get our grid to verify bounds. 
        self.grid = app.grid

        self.cX = cX
        self.cY = cY
        self.cAngle = cAngle # Face in right direction
        self.cRadius = 4 # tank's barrel is 8 pxls

        # Change in dX and dY
        # Zero points to left, so flip sign of dX and dY
        self.dX = -5 * (math.cos(self.cAngle))
        self.dY = -5 * (math.sin(self.cAngle))

        self.bounceAmount = 0

    def drawProjectile(self, app):
        # Create our projectile
        drawCircle(self.cX, self.cY, self.cRadius, fill = 'grey')
    
    def onStep(self):
        # Handle bounces
        self.cX += self.dX
        self.cY += self.dY
        
    # Helper to control bound movements
    def checkCollision(self, app):
        # Look three points ahead
        newX = self.cX + self.dX
        newY = self.cY + self.dY

        if ((0 <= newX < self.grid.gWidth) and (0 <= newY < self.grid.gHeight)
             and self.grid.checkPoint(int(newX), int(newY))):
            return True

        
        else: # New position doesn't work. 
            if self.bounceAmount < 1: 
                # Check whehter it's x or y that's the problem
                if ((not 0 <= self.cX < self.grid.gWidth) 
                     or self.grid.checkPoint(int(self.cX), int(newY))):
                    self.dX *= -1
                
                # run this as an if later
                elif ((not 0 <= self.cY < self.grid.gHeight)
                      or self.grid.checkPoint(int(newX), int(self.cY))):
                    self.dY *= -1

                # update bounce count
                self.bounceAmount += 1                 
                return True
            
            else:
                # If both cases fail, 
                return False