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

        # Red ribbon starts around 530 pxls
        self.gHeight = app.height - 72 

        # CELL HEIGHT/WIDTH should be 33 HIGH * 40 WIDE
        self.rows = 16
        self.cols = 20

        self.cWidth = self.gWidth // self.cols
        self.cHeight = self.gHeight // self.rows

        # Edited Wood Photo from Free Stock photos by Vecteezy 
        # Inspired from Basic PIL Methods. 
        # "https://www.vecteezy.com/free-photos"
        self.background = CMUImage(Image.open('Images\Background.png'))


        # Grid map inspired from Wii Tanks' map on Mission 17
        #https://tanks.brightsoo.com/mission17/
        self.gridMap = [
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]


    def redraw(self, app):
        drawImage(self.background, app.width // 2, app.height // 2,
                  align = 'center') 
        # drawRect(0, 0, app.width, app.height, fill = rgb(210, 251, 142))
        self.drawDrawGrid(app)

    # Code influenced from homework lesson 5.3.2 Drawing a 2D Board
    # https://cs3-112-f22.academy.cs.cmu.edu/notes/4187
    def rowColToXY(self, row, col):
        xVal = self.gLeft + (self.cWidth * col)
        yVal = self.gTop + (self.cHeight * row)
        return ((xVal, yVal))

    # Grid code inspired from homework lesson 5.3.2 Drawing a 2D Board
    # https://cs3-112-f22.academy.cs.cmu.edu/notes/4187
    def drawDrawGrid(self, app):
        for row in range(len(self.gridMap)):
            for col in range(len(self.gridMap[row])):
                cellTop = self.gTop + (self.cHeight * row)
                cellLeft = self.gLeft + (self.cWidth * col)
                cCol = rgb(242, 225, 185)
                cBorder = rgb(205, 179, 119)

                if self.gridMap[row][col] == 1:
                    drawRect(cellLeft, cellTop, self.cWidth, self.cHeight,
                              fill = cCol, border = cBorder, borderWidth = 5)
        
    # Check if a point crosses any of the obstacles. 
    def checkPoint(self, pointX, pointY):
        # Edge Case: if the values pass the width or the height
        if (not 0 <= pointX < self.gWidth) or (not 0 <= pointY < self.gHeight):
            return False

        # get the row / column of the where pointX, pointY is. 
        col = (pointX // self.cWidth)
        row = (pointY // self.cHeight)
        location = self.gridMap[row][col]
        
        # If there's a block, return false
        if location == 1: 
            return False
        else:
            return True
