# Class the manages all the projectiles that are in the game
# Should have permissions to remove projectiles, and call kill functions
from cmu_graphics import *

class ProjectileManager:
    def __init__(self, app):
        self.objects = app.objects

        # Other classes will add to this list
        self.projectiles = []

    def onStep(self, app):
        # First check that it's not empty
        for projectile in self.projectiles:
            # if in bounds
            if projectile.checkCollision(app):  
                for object in self.objects:
                    # Check collision of targets
                    check = object.checkHit(projectile)
                    if check:
                        projectile.onStep()
                    
                    else:
                        # Get rid of the object. 
                        self.objects.remove(object)

            else: self.projectiles.remove(projectile)

    def redraw(self, app):
        for projectile in self.projectiles:
            projectile.drawProjectile(app)


