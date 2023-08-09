# Game that controls what we do when running actual gameplay
from cmu_graphics import *
from Player import *
from Enemy import *
from Enemies.RedEnemy import *
from Enemies.YellowEnemy import *
from Enemies.GreenEnemy import *
from Projectile import * 
from ProjectileManager import *
from Grid import *


class RunGame:
    def __init__(self, app):
        print('Gameplay Created')
        self.restartApp(app)
        print(app.gameOver, app.paused)


    def restartApp(self, app):
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
        # Add enemies at appropiate locations. 
        app.objects.append(Enemy(app.enemyCoords[0][0], app.enemyCoords[0][1]))
        app.objects.append(GreenEnemy(app.enemyCoords[1][0], app.enemyCoords[1][1]))
        app.objects.append(RedEnemy(app.enemyCoords[2][0], app.enemyCoords[2][1]))

        app.objects.append(YellowEnemy(app.enemyCoords[3][0], app.enemyCoords[3][1]))
        app.objects.append(GreenEnemy(app.enemyCoords[4][0], app.enemyCoords[4][1]))
        app.objects.append(RedEnemy(app.enemyCoords[5][0], app.enemyCoords[5][1]))


    def onStep(self):
        if not app.gameOver and not app.paused:
            app.projectileManager.onStep(app)
            for object in app.objects:
                object.onStep(app)
        
        elif app.gameOver:
            # Run explosion
            app.currentScene = app.runScenes[4]

    def redraw(self, app):
        app.grid.redraw(app)
        app.projectileManager.redraw(app)
        for object in app.objects:
            object.redraw(app)
    
    def keyHold(self, keys):
        if not app.gameOver and not app.paused:
            for object in app.objects:
                object.keyHold(keys)

    def mousePress(self, mouseX, mouseY):
        if not app.gameOver and not app.paused:
            for object in app.objects:
                object.mousePress(mouseX, mouseY)
            
    def mouseMove(self, mouseX, mouseY):
        if not app.gameOver and not app.paused:
            # We just want the player
            for object in app.objects:
                object.mouseMove(mouseX, mouseY)

    def keyPress(self, key):
        # We want these functionality to only be sent when we're playing
        if key == 'p':
            app.paused = not app.paused


