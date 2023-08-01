from cmu_graphics import *

''' 
* Toy Tanks
* CMU 15112 Term Project
* Author: Yifan Jiang
* Date: 10 August 2023
*
'''

def onAppStart(app):
    pass

def onMousePress(app, mouseX, mouseY):
    pass

def onKeyPress(app, key):
    pass

def redrawAll(app):
    drawRect(app.width // 2, app.height // 2, 40, 30, align = 'center',
             fill = 'darkBlue')
    pass

def main():
    runApp(width = 800, height = 600)

main()