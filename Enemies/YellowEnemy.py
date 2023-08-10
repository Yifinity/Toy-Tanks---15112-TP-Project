from Enemies.Enemy import *

class YellowEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.color = 'lemonChiffon'
        self.border = 'gold'

        # Fire frequency = seconds per shot. 
        self.fireFrequency = 2
