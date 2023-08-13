from cmu_graphics import *
from PIL import Image
from Data.Player import *

class Introduction:
    def __init__(self):
        # Check if intro is over        
        self.titleOver = False

        # Scrolling Background 
        # https://stock.adobe.com/search?k=wood+texture+seamless&asset_id=275112044
        self.background = CMUImage(Image.open('Data\Images\whiteBackground.jpg'))

        # Test tank
        self.testUserX = app.width // 2
        self.testUserY = app.height // 2 + 100
        self.degrees = 0
        self.dAngle = 3

        self.tankWidth = 140
        self.tankHeight = 120

        # inspiration for a scrolling background
        # https://www.youtube.com/watch?v=ARt6DLP38-Y
        self.firstBgX = 0
        self.secondBgX = app.width
        
        # Photo is a snipped photo of the tank during the game with the 
        # background removed
        self.testUser = CMUImage(Image.open('Data\Images\TestTank.png').rotate(180))

        # Opacity 
        # Same copy and paste code from instruction. 
        self.startOpacity = 95
        self.dO = -5

        self.sceneOpacity = 100
    def redraw(self, app):        
        drawImage(self.background, self.firstBgX, 0, height = app.height,
                  opacity = self.sceneOpacity, width = app.width)
        
        drawImage(self.background, self.secondBgX, 0, width = app.width,
                 opacity = self.sceneOpacity, height = app.height)

        drawLabel("Toy Tanks", app.width // 2, app.height // 2 - 100, 
                  align = 'center', size = 150, fill = rgb(242, 225, 185), 
                  opacity = self.sceneOpacity,
                  bold = True, border = 'black', borderWidth = 2)
        
                # Show a image of the tank the user can control 
        drawImage(self.testUser, self.testUserX, self.testUserY,
                  width = self.tankWidth, height = self.tankHeight,
                  opacity = self.sceneOpacity,
                  align = 'center', rotateAngle = self.degrees)
        
        drawLabel("Press [Space] to Begin", 
                  app.width // 2, app.height // 2 + 150, align = 'center',
                  size = 50, opacity = self.startOpacity, bold = True)
    
    def onStep(self):
        # Move our continously scrolling background
        self.firstBgX -= 10
        self.secondBgX -= 10

        if self.secondBgX <= 0:
            # reset the background
            self.secondBgX = app.width
            self.firstBgX = 0
        
        if not self.titleOver:
            # Have the text fade in and out
            if (self.startOpacity >= 95 and self.dO > 0
               or self.startOpacity <= 5 and self.dO < 0):
                self.dO *= -1
                self.startOpacity += self.dO
            
            self.startOpacity += self.dO
        
        else:
            if self.sceneOpacity > 0:
                # Have everything fade out
                self.sceneOpacity -= 5
            
            else:
                # once that's done, switch the screen
                app.currentScene = app.runScenes[2]
    
    def keyPress(self, key):
        if key == 'space':
            # First make sure the label's opactity is 0
            self.startOpacity = 0
            
            # Start the fade out animation
            self.titleOver = True


    def mousePress(self, mouseX, mouseY):
        pass

    def mouseMove(self, mouseX, mouseY):
        pass

    def keyHold(self, keys):
        pass