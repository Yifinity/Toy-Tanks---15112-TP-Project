# Class the manages all the projectiles that are in the game
# Should have permissions to remove projectiles, and call kill functions
from cmu_graphics import *
from Data.Enemies.Enemy import * 
from Data.Enemies.GreenEnemy import * 
from Data.Enemies.YellowEnemy import *
from Data.Enemies.RedEnemy import * 
from Data.Tank import distance

import random

# Copy and pasted from Professor Ray's SoundTest.py
import os, pathlib

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

        # Music below from Video Game Music
        #https://downloads.khinsider.com/game-soundtracks/album/wii-play
        app.missionEnd = self.loadSound("Data\Sounds\MissionEnd.mp3")
        app.runMission = self.loadSound("Data\Sounds\GamePlay.mp3")

        # Music From The Sounds Resource
        # https://www.sounds-resource.com/wii/wiiplay/sound/28569/?source=genre
        app.userShot = self.loadSound("Data\Sounds\_UserShot.mp3")
        app.enemyShot = self.loadSound("Data\Sounds\_EnemyShot.mp3")

    
    # Copy and Pasted Professor Ray's Code for Method
    def loadSound(self, relativePath):
        # Convert to absolute path (because pathlib.Path only takes absolute paths)
        absolutePath = os.path.abspath(relativePath)
        # Get local file URL
        url = pathlib.Path(absolutePath).as_uri()
        # Load Sound file from local URL
        return Sound(url)

    def addMissile(self, missile):
        self.projectiles.append(missile)

    def onStep(self, app):
        self.stepCount += 1

        # Check if the timer has fired the queue has tanks
        if (len(self.tankQueue) != 0 and (self.stepCount / 60 >= self.secCount 
                                          or len(self.objects) < 5)):
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

                            app.runMission.pause()
                            app.missionEnd.play()
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
        # Remove that location, as we are going to use it to spawn a tank. 
        self.removedLocations.remove((cordX, cordY))
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
        newIdx = 0
        nextEnemy = self.tankQueue[newIdx]

        # Check if our tank is there so we don't pop into their vicinity
        if self.isTankThere(nextEnemy.x, nextEnemy.y):
            if len(self.tankQueue) >= 2:

                # move the failed object to the end of the list
                self.tankQueue.append(nextEnemy)
                self.tankQueue.pop(0)

            else:
                return 

        # Run normally with the next tank at index 0
        self.objects.append(self.tankQueue[newIdx])
        self.tankQueue.pop(newIdx)


    # Check to see if there is a tank is within the vacinity of the coordinates
    def isTankThere(self, cordX, cordY):
        distance = Tank.distance(app.user.x, app.user.y, cordX, cordY)
        if distance <= 50:
                return True
        return False
    
