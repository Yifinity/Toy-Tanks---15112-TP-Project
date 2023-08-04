# Grid class that creates a map for the user to interact on 
from cmu_graphics import *
# from PIL import Image

class Grid:
    def __init__(self, app):
        self.margin = 20
        self.gLeft = 0
        self.gTop = 0
        self.gWidth = app.width

        # Red ribbon starts around 533 pxls
        self.gHeight = app.height - 67 

        self.rows = 20
        self.cols = 16

        self.cWidth = self.gWidth // self.rows
        self.cHeight = self.gHeight // self.cols

        print(f'LOWEST POINT = {self.gTop + self.gHeight}')
        # Edited Wood Photo from Free Stock photos by Vecteezy 
        # "https://www.vecteezy.com/free-photos"
        self.woodUrl = 'Images\Background.png'


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
        drawImage(self.woodUrl, app.width // 2, app.height // 2, align = 'center') 
        # drawRect(0, 0, app.width, app.height, fill = rgb(210, 251, 142))
        self.drawDrawGrid(app)

    # Grid code inspired from homework lesson 5.3.2 Drawing a 2D Board
    # https://cs3-112-f22.academy.cs.cmu.edu/notes/4187
    def drawDrawGrid(self, app):
        for row in range(len(self.gridMap)):
            for col in range(len(self.gridMap[row])):
                cellTop = self.gTop + (self.cHeight * row)
                cellLeft = self.gLeft + (self.cWidth * col)
                cellCol = rgb(243, 242, 208)
                borderCol = rgb(235, 233, 183)


                if self.gridMap[row][col] == 1:
                    # Draw an image if value is 1
                  drawRect(cellLeft, cellTop, self.cWidth, self.cHeight, 
                            fill = cellCol, border = borderCol, borderWidth = 1)

                    # drawImage(self.woodUrl, cellLeft, cellTop, align = 'left', 
                            # width = self.cWidth, height = self.cHeight)

                # else:

                    # # print(f'Cell {row + col} at: {cellLeft, cellTop}')
  
                
                
    # def drawGrid(
        
    # )
