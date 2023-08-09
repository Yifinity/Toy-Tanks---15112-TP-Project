from cmu_graphics import *
from PIL import Image

class Instructions:
    def __init__(self):
        self.visible = False
        self.count = 180
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

        # Test tank



    def redraw(self, app):
        drawLabel("Instructions", self.startTextX, self.startTextY,
                   size = 30, bold = True)
        
        drawLabel("Use the WS Keys to move forward and backwards", 
                  self.instructionX, self.wdYPos, font = 'orbitron', size = 15)

        drawImage(self.wKeyIcon, self.startTextX, self.iconWSY, align = 'center', 
                  height = self.iconSize, width = self.iconSize) 
        
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
        
    def keyPress(self, key):
        if key == 'r':
            self.visible = True


    def onStep(self):
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
        pass