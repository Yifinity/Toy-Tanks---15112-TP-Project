from Player import *

''' 
* Toy Tanks
* CMU 15112 Term Project
* Author: Yifan Jiang
* Date: 10 August 2023
*
'''

def onAppStart(app):
    # Send in our player as our first object 
    app.objects = [Player()]

def redrawAll(app):
    for object in app.objects:
        object.redraw(app)

def onMousePress(app, mouseX, mouseY):
    pass

def onMouseMove(app, mouseX, mouseY):
    # We just want the player
    app.objects[0].mouseMove(mouseX, mouseY)


def onKeyPress(app, key):
    for object in app.objects:
        object.keyPress(key)


def onKeyHold(app, keys):
    for object in app.objects:
        object.keyHold(keys)

def main():
    runApp(width = 800, height = 600)

main()