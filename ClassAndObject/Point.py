import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return (f'({self.x}, {self.y})')

    def getDistance(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def getQuadrant(self):
        if self.x > 0 and self.y > 0:
            print(f'The point is in quadrant I')
        if self.x > 0 and self.y < 0:
            print(f'The point is in quadrant IV')
        if self.x < 0 and self.y < 0:
            print(f'The point is in quadrant III')
        if self.x < 0 and self.y > 0:
            print(f'The point is in quadrant II')

    def move(self, deltax, deltay):
        self.x += deltax
        self.y += deltay
        print(f'The new point is at ({self.x}, {self.y})')

    def getDistanceBetween(cls, p1, p2):
        if p1.x > p2.x:
            a = p1.x - p2.x
        else:
            a = p2.x - p1.x
        if p1.y > p2.y:
            b = p1.y - p2.y
        else:
            b = p2.y - p1.y
        c = math.sqrt(a**2 + b**2)
        return c

class Point3D(Point):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def dot3D(self, x, y, z):
        d = math.sqrt(x**2 + y**2 + z**2)
        return d

point1 = Point(2, 2)
point2 = Point(5, 6)
point3 = Point3D(2, 3, 4)
print(point1.getDistance())
point1.move(0, 0)
point1.getQuadrant()
print(point1.getDistanceBetween(point1, point2))
print(point3.dot3D(2, 6, 9))
