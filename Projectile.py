from cmu_graphics import *
import math
# from Player import *

class Projectile:
    def __init__(self, cX, cY, cAngle):
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
        # if we bounce more than 2 times, destroy the projectile
        # if we're inside bounds
        if (0 <= self.cX < app.width) and (0 <= self.cY < app.height):
            return True

        # Projectile is outside. 
        else:
            self.bounceAmount += 1 # update bounce count
            if self.bounceAmount < 2: 
                # Reverse direction
                if not (0 <= self.cX < app.width):
                    self.dX *= -1
                
                if not (0 <= self.cY < app.height):
                    self.dY *= -1

                return True
            
            else:
                # If both cases fail, 
                return False