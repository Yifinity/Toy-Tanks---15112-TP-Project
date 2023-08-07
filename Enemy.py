from Tank import *
from math import *
from Line import *

class Enemy(Tank):
    def __init__(self, x, y):
        super().__init__(x, y)

        # Default that I may change. 
        self.availableProjectiles = 5
        self.color = 'seaGreen'
        self.border = 'darkGreen'

        self.differenceX = 0
        self.differenceY = 0
        self.turretDegrees = 0


    def onStep(self, app):
        self.targetUser() 
                          

    def targetUser(self):
        # user will always be the first object in objects
        # Point at the user
        user = self.objects[0]
        self.tX = user.x
        self.tY = user.y

        self.differenceX = self.x - user.x
        self.differenceY = self.y - user.y

        turretRads = math.atan2(self.differenceY, self.differenceX)

        if self.notBlocked(user):
            self.tubeX = self.x - self.tubeDistance * math.cos(turretRads)
            self.tubeY = self.y - self.tubeDistance * math.sin(turretRads)
            
            # Turn it to degrees for the turret to rotate. 
            self.turretDegrees = math.degrees(turretRads)



    # Check if the turret's view is blocked by a wall. 
    def notBlocked(self, user):
        # Create a line of fire from the enemy to the user 
        lineOfFire = Line((self.x, self.y), (user.x, user.y))
        for (x, y) in lineOfFire.points:
            # Check if each point on the line of fire is blocked 
            if not self.grid.checkPoint(int(x), int(y)):
                return False
        
        return True