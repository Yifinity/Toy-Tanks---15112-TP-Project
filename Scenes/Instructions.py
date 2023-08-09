from cmu_graphics import *
from PIL import Image

class Instructions:
    def __init__(self):
        self.visible = False
        self.count = 180
        self.timer = 0

        self.startTextX = 200
        self.startTextY = 100

        # The following key images are taken from IconExperience:
        # https://www.iconexperience.com/v_collection/icons/?icon=keyboard_key_w
        self.wKeyIcon = CMUImage(Image.open('Images\WKey.png'))

        # https://www.iconexperience.com/v_collection/icons/?icon=keyboard_key_s
        self.sKeyIcon = CMUImage(Image.open('Images\SKey.png'))

        # https://www.iconexperience.com/v_collection/icons/?icon=keyboard_key_d
        self.dKeyIcon = CMUImage(Image.open('Images\DKey.png'))

        # https://www.iconexperience.com/v_collection/icons/?icon=keyboard_key_a
        self.aKeyIcon = CMUImage(Image.open('Images\AKey.png'))


    def redraw(self, app):
        drawLabel("Instructions", self.startTextX, self.startTextY,
                   size = 30, bold = True)
        
        drawLabel("Use the WD Keys to move back and forth", app.width // 2, 
                app.height // 2, size = 15)

        drawImage(self.wKeyIcon, 200, app.height // 2, 
                  height = 50, width = 50, align = 'center') 
    
        drawLabel("Use the Mouse to Aim and Shoot!", app.width // 2, 
                app.height // 2, size = 30, bold = True)
        
        drawLabel("Press r To Continue", app.width // 2, 
                app.height // 2 + 100, size = 30, bold = True)
        
        drawLabel(f'Starting in {self.timer}', app.width // 2, 
                app.height // 2 + 200, size = 60, bold = True, visible = self.visible)
        

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