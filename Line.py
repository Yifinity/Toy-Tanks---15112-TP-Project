# Create class that enables y = mx + b features like evaluating numbers
from Player import *
from Projectile import *

class Line:
    # Point 1 and point 2 should be tuples of x and y cords
    def __init__(self, point1, point2):
        self.point1X = point1[0]
        self.point1Y = point1[1]

        self.point2X = point2[0]
        self.point2Y = point2[1]
        
        dX = self.point2X - self.point1X
        dY = self.point2Y - self.point1Y

        self.slope = dY / dX
        self.yIntercept = self.point1Y - (self.slope * self.point1X)

        self.points = []

        leftmostPoint = min(self.point1X, self.point2X)
        rightmostPoint = max(self.point1X, self.point2X)

        # Add every point on the line to self.points
        for xVal in range(int(leftmostPoint), int(rightmostPoint)):
            yVal = (self.slope * xVal) + self.yIntercept
            self.points.append((xVal, yVal))

    def evaluatePoint(self, startIdx, projectile):
        # using our good fashioned y = mx + b
        evaluatedY = (self.slope * projectile.cX) + self.yIntercept

        # for the point to be in the shapes
        # cY should be higher at poitns 0 and 3
        # and cY should be lower at points 1 and 2
        if startIdx == 0 or startIdx == 3:
            return (projectile.cY >= evaluatedY)
            
        elif startIdx == 1 or startIdx == 2:
            return (projectile.cY <= evaluatedY)

    


