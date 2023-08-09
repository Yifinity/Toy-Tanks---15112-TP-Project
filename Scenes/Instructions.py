from cmu_graphics import *
from PIL import Image
from Player import *

class Instructions:
    def __init__(self):
        self.visible = False
        self.count = 240
        self.timer = 0

        # Coordinates for the text Instructions
        self.startTextX = 200
        self.startTextY = 100

        # X pos of various instruction steps
        self.instructionX = app.width // 2

        # Y position of the instructions for WS
        self.wdYPos = self.startTextY + 75

        self.iconWSY = self.wdYPos - 12.5
        self.iconSize = 25

        # Y position of the icon for AD
        self.iconADX = self.startTextX - 12.5
        self.iconADY = self.iconWSY + 75

        self.mouseInstructY = self.iconADY + 50

        # Y position for text telling you to press space to start
        self.readyY = self.mouseInstructY + 175
        self.readyOpacity = 95
        self.dO = -1.5

        # Icon Images
        # The following key images are taken from IconExperience:
        # https://www.iconexperience.com/v_collection/icons/?icon=keyboard_key_w
        self.wKeyIcon = CMUImage(Image.open('Images\Keys\WKey.png'))

        # https://www.iconexperience.com/v_collection/icons/?icon=keyboard_key_s
        self.sKeyIcon = CMUImage(Image.open('Images\Keys\SKey.png'))

        # https://www.iconexperience.com/v_collection/icons/?icon=keyboard_key_d
        self.dKeyIcon = CMUImage(Image.open('Images\Keys\DKey.png'))

        # https://www.iconexperience.com/v_collection/icons/?icon=keyboard_key_a
        self.aKeyIcon = CMUImage(Image.open('Images\Keys\AKey.png'))

        # Draw Background
        # Edited Wood Photo from Free Stock photos by Vecteezy 
        # Inspired from Basic PIL Methods. 
        # "https://www.vecteezy.com/free-photos"
        self.background = CMUImage(Image.open('Images\Background.png'))

        # Test tank
        self.testUserX = self.instructionX
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
        
        drawLabel("Instructions", self.startTextX, self.startTextY,
                   size = 30, bold = True)
        
        drawLabel("Use the WS Keys to move forward and backwards", 
                  self.instructionX, self.wdYPos, font = 'orbitron', size = 15)

        drawImage(self.wKeyIcon, self.startTextX, self.iconWSY, 
                  align = 'center', height = self.iconSize,
                  width = self.iconSize) 
                  
        
        drawImage(self.sKeyIcon, self.startTextX, self.iconWSY + 25,  
                  align = 'center', height = self.iconSize,
                  width = self.iconSize) 
        
        drawImage(self.aKeyIcon, self.iconADX, self.iconADY, align = 'center', 
                  height = self.iconSize, width = self.iconSize) 
        
        drawImage(self.dKeyIcon, self.iconADX + 25, self.iconADY,  
                  align = 'center', height = self.iconSize,
                  width = self.iconSize) 
        
        drawLabel("Use the AD Keys to rotate left and right", 
                  self.instructionX, self.iconADY, font = 'orbitron', size = 15)
        

        drawLabel("Move the Mouse to Aim and Shoot (Feature Not Avaliable)",
                  self.instructionX, self.mouseInstructY, font = 'orbitron',
                  size = 15)
        
        drawLabel("Press [Space] to Start", self.instructionX, self.readyY, 
                  font = 'orbitron', opacity = self.readyOpacity, bold = True,
                  size = 25, visible = not self.visible)

                # Show a image of the tank the user can control 
        drawImage(self.testUser, self.testUserX, self.testUserY,
                  width = self.tankWidth, height = self.tankHeight,
                  align = 'center', rotateAngle = self.degrees)
        
        drawLabel(str(self.timer), self.instructionX, app.height // 2, 
            font = 'orbitron', opacity = self.readyOpacity, bold = True,
            size = 150, visible = self.visible)
        
    def keyPress(self, key):
        if key == 'space':
            self.visible = True

    def onStep(self):
        # Create a changing opacity animation
        if (self.readyOpacity >= 95 and self.dO > 0
            or self.readyOpacity <= 5 and self.dO < 0):
            self.dO *= -1
            self.readyOpacity += self.dO
        
        self.readyOpacity += self.dO

        if self.visible:
            self.count -= 1
            self.timer = self.count // 60

            if self.count == 0:
                app.currentScene = app.runScenes[3]


    def mousePress(self, mouseX, mouseY):
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
