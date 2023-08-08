from Enemy import *

class GreenEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.color = 'lightSeaGreen'
        self.border = 'teal'
        # Fire frequency = seconds per shot. 
        self.fireFrequency = 1.5
