''' 
* Toy Tanks
* CMU 15112 Term Project
* Author: Yifan Jiang
* Date: 10 August 2023
'''
from Player import *
from Projectile import * 
from Grid import *


def onAppStart(app):
    # Use 60 sets per second for easy conversiond
    app.stepsPerSecond = 60
    # Send in our player as our first object 
    app.grid = Grid(app)
    app.user = Player(app.grid)
    app.objects = [app.user]


def redrawAll(app):
    app.grid.redraw(app)
    for object in app.objects:
        object.redraw(app)

def onStep(app):
    for projectile in app.user.projectiles:
        if projectile.checkCollision(app): # if it does work, 
            projectile.onStep()
        
        else:
            app.user.projectiles.remove(projectile)

    for object in app.objects:
        object.onStep(app)

def onMousePress(app, mouseX, mouseY):
    app.user.mousePress(mouseX, mouseY)

def onMouseMove(app, mouseX, mouseY):
    # We just want the player
    app.user.mouseMove(mouseX, mouseY)

def onKeyPress(app, key):
    for object in app.objects:
        object.keyPress(key)

def onKeyHold(app, keys):
    for object in app.objects:
        object.keyHold(keys)
    

def main():
    runApp(width = 800, height = 600)

main()