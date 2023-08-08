from cmu_graphics import *
from PIL import Image


class Startup:
    def __init__(self):
        self.isOver = False
        self.counter = 0
        self.targetTime = 5

        # Animation Taken from previous Tetris Project
        self.textY = app.height // 2 - 20
        self.arrowX = app.width // 2 + 95

        self.titleOpacity = 0

                # Edited Wood Photo from Free Stock photos by Vecteezy 
        # Inspired from Basic PIL Methods. 
        # "https://www.vecteezy.com/free-photos"
        self.arrow = CMUImage(Image.open('Images\Arrow.png'))


    

    def redraw(self, app):
        drawLabel("Yifinity", app.width // 2, self.textY,
                align = 'bottom', size = 40, font = 'orbitron', bold = True, 
                opacity = self.titleOpacity)
        drawImage(self.arrow, self.arrowX, app.height // 2 - 20, height = 42.5, 
                  width = 42.5, align = 'center') 

    
    def onStep(self):
        if self.titleOpacity < 100:
            # Increase opacity
            self.titleOpacity += 10
            self.textY += 2
        else:
            if self.counter < 45:
                self.counter += 1
                # Move the arrow to the right
                arrowDistance = ((app.width - self.arrowX) + 20) // 20
                self.arrowX += arrowDistance 

            elif self.counter < 60:
                self.counter += 2

            else:
                self.isOver = True    

    def onMousePress(app, mouseX, mouseY):
        pass

    def onMouseMove(app, mouseX, mouseY):
        pass

    def keyPress(self, key):
        pass

    def keyHold(self, keys):
        pass