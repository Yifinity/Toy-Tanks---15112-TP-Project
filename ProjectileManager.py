# Class the manages all the projectiles that are in the game
# Should have permissions to remove projectiles, and call kill functions
from cmu_graphics import *
from Enemies.Enemy import * 
from Enemies.GreenEnemy import * 
from Enemies.YellowEnemy import *
from Enemies.RedEnemy import * 
from Tank import distance

import random

class ProjectileManager:
    def __init__(self, app):
        self.objects = app.objects

        # Other classes will add to this list
        self.projectiles = []
        self.stepCount = 0
        
        # Spawn Variables
        self.secCount = 1.5 # Get the seconds needed to spawn a new tank
        self.tankQueue = []
        self.removedLocations = []
        self.sampleSize = 50

    def addMissile(self, missile):
        self.projectiles.append(missile)

    def onStep(self, app):
        self.stepCount += 1

        # Check if the timer has fired the queue has tanks
        if (len(self.tankQueue) != 0 and (self.stepCount / 60 >= self.secCount 
                                          or len(self.objects) < 4)):
            self.generateNextTank()
            self.stepCount = 0

        # First check that it's not empty
        for projectile in self.projectiles: 
            if projectile.checkCollision(app): 
                for object in self.objects:
                    # Check if we hit a tank
                    if object.checkHit(projectile): 
                        # Check if we hit grid/or out of bounds
                        projectile.onStep()
                    
                    else:
                        if object == app.user:
                            app.gameOver = True
                        else:
                            app.userScore += 1
                            self.addNextTank(object)
                            self.stepCount = 0

                        self.projectiles.remove(projectile)
                        return
            else:
                # If we fail the grid-boundary test
                self.projectiles.remove(projectile)
                return


    def redraw(self, app):
        for projectile in self.projectiles:
            projectile.drawProjectile(app)

    def addNextTank(self, enemy):
        # Add a tuple of locations where the enemy was shot
        self.removedLocations.append((enemy.x, enemy.y))

        # Remove the enemy
        self.objects.remove(enemy)

        # if we only have one point, don't use that point, and simply move on
        if len(self.removedLocations) < 2: return 

        # Get a coodinate randomly from the removed location.         
        (cordX, cordY) = random.choice(self.removedLocations)        
        self.removedLocations.remove((cordX, cordY))

        if self.isTankThere(cordX, cordY): return 

        # should be 25 to around 125 - increase difficulty with higher score
        self.sampleSize =  app.userScore * 10
        selection = random.randint(0, self.sampleSize)

        # Scores between 0-2
        if selection < 20:
            self.tankQueue.append(Enemy(cordX, cordY))

        # Scores between 3 - 6
        elif selection < 50:
            self.tankQueue.append(YellowEnemy(cordX, cordY))

        # Scores between 7 - 12
        elif selection < 80:
            self.tankQueue.append(GreenEnemy(cordX, cordY))

        else:
            self.tankQueue.append(RedEnemy(cordX, cordY))


    # Remove the enemy and add a new one
    def generateNextTank(self):
        self.objects.append(self.tankQueue[0])
        self.tankQueue.pop(0)


    # Check to see if there is a tank is within the vacinity of the coordinates
    def isTankThere(self, cordX, cordY):
        for tank in self.objects:
            if Tank.distance(cordX, cordY, tank.x, tank.y) <= 35:
                return True
                    
        return True