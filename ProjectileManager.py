# Class the manages all the projectiles that are in the game
# Should have permissions to remove projectiles, and call kill functions
from cmu_graphics import *

class ProjectileManager:
    def __init__(self, app):
        self.objects = app.objects

        # Other classes will add to this list
        self.projectiles = []


    def addMissile(self, missile):
        self.projectiles.append(missile)

    def onStep(self, app):
        # First check that it's not empty
        for projectile in self.projectiles: 
            for object in self.objects:
                    # Check collision of targets
                    check = object.checkHit(projectile)
                    
                    if check: # if we haven't hit an enemy
                        # Check if we hit grid/or out of bounds
                        if projectile.checkCollision(app): 
                            projectile.onStep()
                        
                        else:
                            # If we fail the grid-boundary test
                            self.projectiles.remove(projectile)
                            return
                    
                    else:
                        self.objects.remove(object)
                        self.projectiles.remove(projectile)


    def redraw(self, app):
        for projectile in self.projectiles:
            projectile.drawProjectile(app)


