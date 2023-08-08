from cmu_graphics import *
from PIL import Image


class GameOver:
    def __init__(self):
        # Photo from The Models Resource
        # https://www.models-resource.com/wii/wiiplay/model/41959/
        self.gameOver = CMUImage(Image.open('Images\GameOver.png'))


    def redraw(self, app):
        drawImage(self.gameOver, app.width // 2, app.height // 2, 
                  height = app.height, width = app.width, align = 'center') 
        drawLabel("Game Over! Score " + str(app.userScore), app.width // 2, 
                  app.height // 2, size = 60, bold = True)

    
    def onStep(self):
        pass
    
    def onMousePress(app, mouseX, mouseY):
        pass

    def onMouseMove(app, mouseX, mouseY):
        pass

    def keyPress(self, key):
        pass

    def keyHold(self, keys):
        pass