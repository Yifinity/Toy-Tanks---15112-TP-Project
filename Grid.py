# Grid class that creates a map for the user to interact on 
from cmu_graphics import *

class Grid:
    def __init__(self, app):
        self.margin = 20
        self.gLeft = self.margin
        self.gTop = self.margin
        self.gWidth = app.width - (2 * self.margin)
        self.gHeight = app.height - (2 * self.margin)

        self.rows = 20
        self.cols = 16

        self.cWidth = self.gWidth // self.rows
        self.cHeight = self.gHeight // self.cols

        print(f'Grid: {self.gWidth}, {self.gHeight} | Cell: {self.cWidth}, {self.cHeight}')

        # Grid map inspired from Wii Tanks' map on Mission 8
        #https://tanks.brightsoo.com/missions/
        self.gridMap = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def redraw(self, app):
        self.drawDrawGrid(app)

    # Grid code inspired from homework lesson 5.3.2 Drawing a 2D Board
    # https://cs3-112-f22.academy.cs.cmu.edu/notes/4187
    def drawDrawGrid(self, app):
        for row in range(len(self.gridMap)):
            for col in range(len(self.gridMap[row])):
                cellTop = self.gTop + (self.cHeight * row)
                cellLeft = self.gLeft + (self.cWidth * col)
                cellColor = 'brown' if self.gridMap[row][col] == 0 else 'yellow'
                
                # print(f'Cell {row + col} at: {cellLeft, cellTop}')
                drawRect(cellLeft, cellTop, self.cWidth, self.cHeight, 
                         fill = cellColor)
                
                
    # def drawGrid(
        
    # )
