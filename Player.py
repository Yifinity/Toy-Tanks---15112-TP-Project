from Tank import *

class Player(Tank):
    def __init__(self, app):
        super().__init__()
        
        # Tank:
        self.color = rgb(6, 6, 193)
        self.border = 'darkBlue'

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
        
        #Projectiles
        self.availableProjectiles = 5
        self.pY = 565
        self.pR = 10
        self.pX = app.width // 2 - (2 * 3 * self.pR)


    def redraw(self, app):    
        drawRect(self.x, self.y, self.width, self.height, border = self.border,
                borderWidth = self.borderWidth, fill = self.color, 
                align = 'center', rotateAngle = self.degrees)
        
        drawRect(self.tubeX, self.tubeY, self.tubeLength, self.baseSize,
                 align = 'center', rotateAngle = self.turretDegrees,
                 fill = self.tubeColor, border = self.tubeBorder)
        
        drawCircle(self.x, self.y, self.capRad, fill = self.tubeColor,
                   border = self.tubeBorder)
        
        # Draw the user aim-target    
        drawCircle(self.mX, self.mY, self.mRad, fill = self.mCol,
                   visible = self.mVis, border = self.color, 
                  borderWidth = self.mBorderWidth)
        
        # Show how many projectiles we have 
        for projectIdx in range(self.availableProjectiles):
            pY, pX = self.pY, self.pX + (projectIdx * (3 * self.pR))
            drawCircle(pX, pY, self.pR, fill = 'black')
            

    def mouseMove(self, mouseX, mouseY):     
        self.mX, self.mY = mouseX, mouseY
        self.followTarget()
    
    def onStep(self, app):
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
    
    # Have the turret follow the mouse position. 
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