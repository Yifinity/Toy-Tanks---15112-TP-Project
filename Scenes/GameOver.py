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
        drawLabel("Game Over!", app.width // 2, app.height // 2, size = 60,
                  bold = True)

    def keyPress(self, key):
        if key == 'r':
                # Send back to gameplay scene
                app.currentScene = app.runScenes[3]
                # Tell gameplay scene to restart itself
                app.currentScene.restartApp(app)

    def onStep(self):
        pass
    
    def mousePress(self, mouseX, mouseY):
        pass

    def mouseMove(self, mouseX, mouseY):
        pass


    def keyHold(self, keys):
        pass