''' 
* Toy Tanks
* CMU 15112 Term Project
* Author: Yifan Jiang
* Date: 10 August 2023
'''

from Player import *
from Enemy import *
from Enemies.RedEnemy import *
from Enemies.YellowEnemy import *
from Enemies.GreenEnemy import *
from Projectile import * 
from ProjectileManager import *
from Grid import *
from Scenes.GameOver import *
from Scenes.Startup import *


def onAppStart(app): 
    app.runningAnimation = True
    app.scenes = {
        0 : 'Startup',
        1 : 'Intro', 
        2 : 'CountDown',
        3 : 'Game',
        4 : 'Paused',
        5 : 'GameOver'
    }   

    # Use 60 sets per second for easy conversion factor
    app.stepsPerSecond = 60
    app.currentScene = app.scenes[0]
    app.startup = Startup()
    app.gameOverScene = GameOver()

    restartApp(app)

def restartApp(app):
    app.userScore = 0
    app.gameOver = False
    app.paused = False

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
    # # Add enemies at appropiate locations. 
    app.objects.append(Enemy(app.enemyCoords[0][0], app.enemyCoords[0][1]))
    app.objects.append(GreenEnemy(app.enemyCoords[1][0], app.enemyCoords[1][1]))
    app.objects.append(RedEnemy(app.enemyCoords[2][0], app.enemyCoords[2][1]))

    app.objects.append(YellowEnemy(app.enemyCoords[3][0], app.enemyCoords[3][1]))
    app.objects.append(GreenEnemy(app.enemyCoords[4][0], app.enemyCoords[4][1]))
    app.objects.append(RedEnemy(app.enemyCoords[5][0], app.enemyCoords[5][1]))


def redrawAll(app):
    if app.currentScene == app.scenes[0]:
        app.startup.redraw(app)

    elif app.currentScene == app.scenes[3]:
        # Game scene
        app.grid.redraw(app)
        app.projectileManager.redraw(app)
        for object in app.objects:
            object.redraw(app)
    
    elif app.currentScene == app.scenes[5]:
        app.gameOverScene.redraw(app)
    

def onStep(app):
    if app.currentScene == app.scenes[0]:
        app.startup.onStep()
        if app.startup.isOver:
            app.currentScene = app.scenes[3]
    
    elif app.currentScene == app.scenes[5]:
        app.gameOverScene.onStep()

    elif app.currentScene == app.scenes[3]:
        if not app.gameOver and not app.paused:
            app.projectileManager.onStep(app)
            for object in app.objects:
                object.onStep(app)
        
        elif app.gameOver:
            app.currentScene = app.scenes[5]

        elif app.paused:
            app.currentScene = app.scenes[4]    


def onMousePress(app, mouseX, mouseY):
    if not app.gameOver and not app.paused:
        for object in app.objects:
            object.mousePress(mouseX, mouseY)

def onMouseMove(app, mouseX, mouseY):
    if not app.gameOver and not app.paused:
        # We just want the player
        for object in app.objects:
            object.mouseMove(mouseX, mouseY)

def onKeyPress(app, key):
    if key == 'p':
        app.paused = not app.paused
    if key == 'r':
        if app.gameOver == True:
            restartApp(app)

def onKeyHold(app, keys):
    if not app.gameOver and not app.paused:
        for object in app.objects:
            object.keyHold(keys)
    
def main():
    runApp(width = 800, height = 600)

main()