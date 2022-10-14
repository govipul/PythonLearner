from math import radians
import math


class Orientations:
    pi = 3.14
    def __init__(self, x_pos, y_pos, degree) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_dir, self.y_dir = self.getUnitVectorFromDegree(degree)

    @staticmethod
    def getUnitVectorFromDegree(degree) -> int: # <- This is how we can define the static method 
        # radians = (degree/180) * math.pi
        radians = (degree/180) * Orientations.pi # <- This is a static variable name pi
        return math.sin(radians), - math.cos(radians)
    
    def getNextPos(self) -> int:
        return self.x_pos + self.x_dir, self.y_pos + self.y_dir


myOrientation = Orientations(5, 5, 75)
print(myOrientation.getNextPos())
    