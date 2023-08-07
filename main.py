''' 
* Toy Tanks
* CMU 15112 Term Project
* Author: Yifan Jiang
* Date: 10 August 2023
'''
from Player import *
from Enemy import *
from Projectile import * 
from ProjectileManager import *
from Grid import *


def onAppStart(app):
    # Use 60 sets per second for easy conversion factor
    app.stepsPerSecond = 60

    app.grid = Grid(app)
    app.objects = []
    app.projectileManager = ProjectileManager(app)
    app.objects.append(Player(app.width // 2, app.height // 2))
    restartApp(app)

def restartApp(app):
    app.objects.append(Enemy(200, 500))
    app.objects.append(Enemy(600, 500))
    app.objects.append(Enemy(100, 100))


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
    for object in app.objects:
        object.mousePress(mouseX, mouseY)

def onMouseMove(app, mouseX, mouseY):
    # We just want the player
    for object in app.objects:
        object.mouseMove(mouseX, mouseY)

def onKeyPress(app, key):
    pass

def onKeyHold(app, keys):
    for object in app.objects:
        object.keyHold(keys)
    
def main():
    runApp(width = 800, height = 600)

main()