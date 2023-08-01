from Player import *

''' 
* Toy Tanks
* CMU 15112 Term Project
* Author: Yifan Jiang
* Date: 10 August 2023
*
'''

def onAppStart(app):
    app.user = Player()
    pass

def onMousePress(app, mouseX, mouseY):
    pass

def onKeyPress(app, key):
    app.user.keyPress(key)

def onKeyHold(app, keys):
    app.user.keyHold(keys)    

def redrawAll(app):
    app.user.redraw(app)

def main():
    runApp(width = 800, height = 600)

main()