from cmu_graphics import *
from PIL import Image
from Player import *

class Introduction:
    def __init__(self):
        # Draw Background
        # Edited Wood Photo from Free Stock photos by Vecteezy 
        # Inspired from Basic PIL Methods. 
        # "https://www.vecteezy.com/free-photos"
        self.background = CMUImage(Image.open('Images\Background.png'))

        # Test tank
        self.testUserX = app.width // 2
        self.testUserY = 500
        self.degrees = 0
        self.dAngle = 3

        self.tankWidth = 70
        self.tankHeight = 60

        # Photo is a snipped photo of the tank during the game with the 
        # background removed
        self.testUser = CMUImage(Image.open('Images\TestTank.png').rotate(180))

    def redraw(self, app):        
        drawImage(self.background, app.width // 2, app.height // 2,
                  align = 'center', width = app.width, height = app.height)

        drawLabel("Toy Tanks", app.width // 2, app.height // 2 - 100, 
                  align = 'center', size = 100, fill = rgb(242, 225, 185))
        
                # Show a image of the tank the user can control 
        drawImage(self.testUser, self.testUserX, self.testUserY,
                  width = self.tankWidth, height = self.tankHeight,
                  align = 'center', rotateAngle = self.degrees)
        
    def keyPress(self, key):
        pass

    def onStep(self):
        pass

    def mousePress(self, mouseX, mouseY):
        # Move onto the next scene
        app.currentScene = app.runScenes[2]
        pass

    def mouseMove(self, mouseX, mouseY):
        pass


    def keyHold(self, keys):
        if 'w' in keys:
            self.testUserX += 2 * math.cos(math.radians(self.degrees))
            self.testUserY += 2 * math.sin(math.radians(self.degrees))
            
        elif 's' in keys: 
            self.testUserX -= 2 * math.cos(math.radians(self.degrees))
            self.testUserY -= 2 * math.sin(math.radians(self.degrees))

        if 'a' in keys: 
            self.degrees -= self.dAngle

        elif 'd' in keys:
            self.degrees += self.dAngle    
        
        self.testUserX %= app.width
        self.testUserY %= app.height
