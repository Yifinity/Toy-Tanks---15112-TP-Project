# Grid class that creates a map for the user to interact on 
from cmu_graphics import *
from PIL import Image
import random


class Grid:
    def __init__(self, app):
        self.margin = 20
        self.gLeft = 0
        self.gTop = 0
        self.gWidth = app.width

        # Red ribbon starts around 533 pxls
        self.gHeight = app.height - 70 

        self.rows = 20
        self.cols = 16

        self.cWidth = self.gWidth // self.rows
        self.cHeight = self.gHeight // self.cols

        # Edited Wood Photo from Free Stock photos by Vecteezy 
        # Inspired from Basic PIL Methods. 
        # "https://www.vecteezy.com/free-photos"
        self.background = CMUImage(Image.open('Images\Background.png'))


        # Grid map inspired from Wii Tanks' map on Mission 8
        #https://tanks.brightsoo.com/missions/
        self.gridMap = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]



    def redraw(self, app):
        drawImage(self.background, app.width // 2, app.height // 2, align = 'center') 
        # drawRect(0, 0, app.width, app.height, fill = rgb(210, 251, 142))
        self.drawDrawGrid(app)

    # Grid code inspired from homework lesson 5.3.2 Drawing a 2D Board
    # https://cs3-112-f22.academy.cs.cmu.edu/notes/4187
    def drawDrawGrid(self, app):
        for row in range(len(self.gridMap)):
            for col in range(len(self.gridMap[row])):
                cellTop = self.gTop + (self.cHeight * row)
                cellLeft = self.gLeft + (self.cWidth * col)
            

                if self.gridMap[row][col] == 1:
                    cCol = rgb(242, 225, 185)
                    cBorder = rgb(205, 179, 119)
                    drawRect(cellLeft, cellTop, self.cWidth, self.cHeight,
                              fill = cCol, border = cBorder, borderWidth = 5)

                    # image = self.blocks[0]
                    # drawImage(image, cellLeft, cellTop, border = borderCol,
                    #           width = self.cWidth, height = self.cHeight)
