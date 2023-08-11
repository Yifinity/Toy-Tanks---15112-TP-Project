# Create class that enables y = mx + b features like evaluating numbers
from Data.Player import *
from Data.Projectile import *

class Line:
    # Point 1 and point 2 should be tuples of x and y cords
    def __init__(self, point1, point2):
        self.point1X = point1[0]
        self.point1Y = point1[1]
        self.point2X = point2[0]
        self.point2Y = point2[1]
        
        dX = self.point2X - self.point1X
        dY = self.point2Y - self.point1Y

        # Check if we have a horizontal or vertical line. 
        self.isHorizontal = True if dY == 0 else False
        self.isVertical = True if dX == 0 else False
        self.points = []

        self.leftmostPoint = int(min(self.point1X, self.point2X))
        self.rightmostPoint = int(max(self.point1X, self.point2X))

        if (not self.isHorizontal) and (not self.isVertical): 
            self.slope = dY / dX
            self.yIntercept = self.point1Y - (self.slope * self.point1X)

            # Add every point on the line to self.points
            for xVal in range(self.leftmostPoint, self.rightmostPoint):
                yVal = (self.slope * xVal) + self.yIntercept
                self.points.append((xVal, yVal))
        
        elif self.isHorizontal:
            for xVal in range(self.leftMostPoint, self.rightmostPoint):
                self.points.append((xVal, self.point1Y))

        elif self.isVertical:
            topmostPoint = int(min(self.point1Y, self.point2Y))
            bottommostPoint = int(max(self.point1Y, self.point2Y))

            # Lowervalue is a higher position. 
            for yVal in range(topmostPoint, bottommostPoint):
                self.points.append((self.point1X, yVal))

    # We don't need to worry about horizontal/vertical lines 
    # As the function that uses this doesn't include rotations of 90 degrees
    def evaluatePoint(self, startIdx, projectile):
        # using our good fashioned y = mx + b
        evaluatedY = (self.slope * projectile.cX) + self.yIntercept

        # for the point to be in the shapes
        # cY should be higher at points 0 and 3
        # and cY should be lower at points 1 and 2
        if startIdx == 0 or startIdx == 3:
            return (projectile.cY >= evaluatedY)
            
        elif startIdx == 1 or startIdx == 2:
            return (projectile.cY <= evaluatedY)

    


