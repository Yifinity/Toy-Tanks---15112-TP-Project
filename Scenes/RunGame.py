# Game that controls what we do when running actual gameplay
from cmu_graphics import *
from Player import *
from Enemies.Enemy import *
from Enemies.RedEnemy import *
from Enemies.YellowEnemy import *
from Enemies.GreenEnemy import *
from Projectile import * 
from ProjectileManager import *
from Grid import *



class RunGame:
    def __init__(self, app):
        self.highScore = 0
        self.restartApp(app)

        # label definitions
        self.gameOverY = app.height // 2 - 75
        self.scoreY = self.gameOverY + 50
        self.hiScoreY = self.scoreY + 25

        self.replayY = app.height // 2 + 50

        self.pausedY = app.height // 2 - 15
        self.pressResumeY = self.pausedY + 50

        self.dO = -2.5
        self.readyOpacity = 95

    def restartApp(self, app):
        app.userScore = 0
        app.gameOver = False
        app.paused = False

        app.grid = Grid(app)
        app.objects = []
        app.projectiles = []
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
        app.objects.append(Enemy(app.enemyCoords[1][0], app.enemyCoords[1][1]))
        app.objects.append(Enemy(app.enemyCoords[2][0], app.enemyCoords[2][1]))

        app.objects.append(Enemy(app.enemyCoords[3][0], app.enemyCoords[3][1]))
        app.objects.append(Enemy(app.enemyCoords[4][0], app.enemyCoords[4][1]))
        app.objects.append(Enemy(app.enemyCoords[5][0], app.enemyCoords[5][1]))


    def onStep(self):
        if not app.gameOver and not app.paused:
            app.projectileManager.onStep(app)
            for object in app.objects:
                object.onStep(app)
            
            for projectile in app.projectiles:
                app.projectileManager.checkStep(projectile)
        
        elif app.gameOver:
            # Copy and pasted from Instructions.py
            # Create a changing opacity animation
            if app.userScore > app.highScore:
                app.highScore = app.userScore

            if (self.readyOpacity >= 95 and self.dO > 0
                or self.readyOpacity <= 5 and self.dO < 0):
                self.dO *= -1
                self.readyOpacity += self.dO
            
            self.readyOpacity += self.dO


    def redraw(self, app):
        app.grid.redraw(app)
        app.projectileManager.redraw(app)

        for object in app.objects:
            object.redraw(app)

        # manually draw all prctiles
        for projectile in app.projectiles:
            projectile.drawProjectile(app)


        if app.gameOver:
            drawRect(app.width // 2, app.height // 2, 600, 250,
                     fill = 'maroon', border = 'darkBlue', borderWidth = 10,
                     align = 'center')
            
            drawLabel("Game Over!", app.width // 2, 
                      self.gameOverY, size = 50, bold = True)
            
            drawLabel("Score: " + str(app.userScore), app.width // 2, 
                      self.scoreY, size = 20, bold = True)
            
            drawLabel("High Score: " + str(app.highScore), app.width // 2, 
                      self.hiScoreY, size = 20, bold = True)
            
            # Copy and pasted from instructions.py
            drawLabel("Press [Space] to Play Again", app.width // 2, self.replayY, 
                      font = 'orbitron', opacity = self.readyOpacity,
                       bold = True, size = 25)
            
        elif app.paused:
            drawRect(app.width // 2, app.height // 2, 600, 200,
                     fill = 'maroon', border = 'darkBlue', borderWidth = 10,
                     align = 'center')
            
            drawLabel("[Paused]", app.width // 2, self.pausedY,
                       size = 50, bold = True)
        
            # Copy and pasted from instructions.py
            drawLabel("Press [p] to resume", app.width // 2, self.pressResumeY, 
                      font = 'orbitron', bold = True, size = 25)

    
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
        if key == 'space' and app.gameOver:
            self.restartApp(app)

        # We want these functionality to only be sent when we're playing
        if key == 'p':
            app.paused = not app.paused


