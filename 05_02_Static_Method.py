from math import radians
import math


class Orientations:
    def __init__(self, x_pos, y_pos, degree) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_dir, self.y_dir = Orientations.getUnitVectorFromDegree(degree)

    def getUnitVectorFromDegree(degree) -> int:
        radians = (degree/180) * math.pi
        return math.sin(radians), - math.cos(radians)
    
    def getNextPos(self) -> int:
        return self.x_pos + self.x_dir, self.y_pos + self.y_dir


myOrientation = Orientations(5, 5, 75)
print(myOrientation.getNextPos())
    