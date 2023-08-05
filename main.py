''' 
* Toy Tanks
* CMU 15112 Term Project
* Author: Yifan Jiang
* Date: 10 August 2023
'''
from Player import *
from Projectile import * 
from ProjectileManager import *
from Grid import *


def onAppStart(app):
    # Use 60 sets per second for easy conversion factor
    app.stepsPerSecond = 60

    app.grid = Grid(app)
    app.objects = []
    app.projectileManager = ProjectileManager(app)
    
    # ProjectileManager must be defined before player, and 
    # Grid/Objects must be defined before Projectilemanager, so 
    # Objects is initially blank
    app.user = Player(app)
    app.objects.append(app.user)

def redrawAll(app):
    app.grid.redraw(app)
    app.projectileManager.redraw(app)
    for object in app.objects:
        object.redraw(app)
    


def onStep(app):
    app.projectileManager.onStep(app)
    for object in app.objects:
        object.onStep(app)
    


def onMousePress(app, mouseX, mouseY):
    app.user.mousePress(mouseX, mouseY)

def onMouseMove(app, mouseX, mouseY):
    # We just want the player
    app.user.mouseMove(mouseX, mouseY)

def onKeyPress(app, key):
    pass

def onKeyHold(app, keys):
    app.user.keyHold(keys)
    

def main():
    runApp(width = 800, height = 600)

main()