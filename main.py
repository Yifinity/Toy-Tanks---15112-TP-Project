''' 
* Toy Tanks
* CMU 15112 Term Project
* Author: Yifan Jiang
* Date: 10 August 2023
'''

from Player import *
from Enemy import *
from YellowEnemy import *
from GreenEnemy import *
from Projectile import * 
from ProjectileManager import *
from Grid import *


def onAppStart(app):    
    restartApp(app)

def restartApp(app):
    app.gameOver = False
    # Use 60 sets per second for easy conversion factor
    app.stepsPerSecond = 60

    app.grid = Grid(app)
    app.objects = []
    app.projectileManager = ProjectileManager(app)
    app.user = Player(app.width // 2, app.height // 2)
    app.objects.append(app.user)

    app.enemyCoords = [
        app.grid.rowColToXY(2, 3),
        app.grid.rowColToXY(14, 3),

        app.grid.rowColToXY(2, 10),
        app.grid.rowColToXY(14, 10),

        app.grid.rowColToXY(2, 17),
        app.grid.rowColToXY(14, 17)
    ]
    
    app.objects.append(YellowEnemy(app.enemyCoords[0][0], app.enemyCoords[0][1]))
    # app.objects.append(GreenEnemy(app.enemyCoords[1][0], app.enemyCoords[1][1]))
    # app.objects.append(Enemy(app.enemyCoords[2][0], app.enemyCoords[2][1]))

    # app.objects.append(YellowEnemy(app.enemyCoords[3][0], app.enemyCoords[3][1]))
    # app.objects.append(GreenEnemy(app.enemyCoords[4][0], app.enemyCoords[4][1]))
    # app.objects.append(GreenEnemy(app.enemyCoords[5][0], app.enemyCoords[5][1]))




def redrawAll(app):
    app.grid.redraw(app)
    app.projectileManager.redraw(app)
    for object in app.objects:
        object.redraw(app)
    

def onStep(app):
    if not app.gameOver:
        app.projectileManager.onStep(app)
        for object in app.objects:
            object.onStep(app)
    
    

def onMousePress(app, mouseX, mouseY):
    if not app.gameOver:
        for object in app.objects:
            object.mousePress(mouseX, mouseY)

def onMouseMove(app, mouseX, mouseY):
    if not app.gameOver:
        # We just want the player
        for object in app.objects:
            object.mouseMove(mouseX, mouseY)

def onKeyPress(app, key):
    if key == 'r':
        if app.gameOver == True:
            restartApp(app)

def onKeyHold(app, keys):
    if not app.gameOver:
        for object in app.objects:
            object.keyHold(keys)
    
def main():
    runApp(width = 800, height = 600)

main()