from Enemies.Enemy import *

class RedEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.color = 'salmon'
        self.border = 'fireBrick'
        # Fire frequency = seconds per shot. 
        self.fireFrequency = 0.75
