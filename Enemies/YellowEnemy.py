from Enemy import *

class YellowEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = 'seaGreen'
        self.border = 'darkGreen'

        self.color = 'lightYellow'
        self.border = 'paleGoldenrod'

        # Fire frequency = seconds per shot. 
        self.fireFrequency = 4
